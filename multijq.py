#-*- coding: utf-8 -*-
"""multijq: runs multiple jq selectors as one"""

import jq

class NoContentError(Exception):
    def __init__(self, message="No content was given. Did you forget to call `Executor.set_contents`?"):
        self.message = message
        super().__init__(self.message)

class JQRuntimeError(Exception):
    def __init__(self, message="Oops, looks like there was an error running jq!"):
        self.message = message
        super().__init__(self.message)

class Executor:
    singleSelectorCompiled = None
    contents = None
    def __init__(self, selectors=[], _test=False):
        self._test = _test
        if _test:
            print("Testing, showing verbose output..")
        self.selectors = selectors
        self.single_selector = self.join_selectors()
        self.compiled_selector = jq.compile(self.single_selector)

    def join_selectors(self):
        def __selector_text__(some_key, some_selector):
            return f' {some_key}: (try ({{success: true, result: ({some_selector})}}| {{success,datatype:(.result|type),result}}) catch ({{success: false, error: (.)}}))'
        _joined_selectors = ','.join(__selector_text__(key_, selector_) for key_, selector_ in self.selectors.items())
        joined_selectors =  f'{{ {_joined_selectors} }}'
        if self._test:
            print(f'selector = \n    {joined_selectors}')
        return joined_selectors

    def set_contents(self, contents):
        self.contents = contents
        if self._test:
            print(f'contents = \n    {contents}')

    def run(self):
        if not self.contents:
            raise NoContentError
        try:
            _run = self.compiled_selector.input(self.contents).first()
        except:
            raise JQRuntimeError
        return _run