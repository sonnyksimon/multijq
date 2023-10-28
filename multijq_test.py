import multijq
import json

selectors = {
    'expectingArray': ".data",
    'expectingObject': ".data[0]",
    'expectingNull': ".data[3]",
    'expectingError': ".data/0"
}
executor = multijq.Executor(selectors=selectors, _test=False)
executor.set_contents({
    "data": [
        {
            "name": "hello",
            "body": "Hello, world!"
        },
        {
            "name": "test",
            "body": "This is a test!"
        }
    ]
})
result = executor.run()
print(json.dumps(result, indent=2))