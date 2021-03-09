# gRPC-helloworld Server

## Prerequisites
- Python 3.5 or higher
- `pip` version 9.0.1 or higher

If necessary, upgrade your version of `pip`:

```bash
python -m pip install --upgrade pip
```

Install gRPC and gRPC tools

```bash
pip install -r requirements.txt
```

## Generate gRPC code
```bash
python -m grpc_tools.protoc -I./protos/helloworld --python_out=. --grpc_python_out=. ./protos/helloworld/hello_world.proto
```

## Run!

```bash
python greeter_server.py
```