from diagrams import Diagram
from diagrams.aws.compute import EC2

with Diagram("Simple Diagram Multi Output", outformat=["jpg", "png", "dot"]):
    EC2("web")