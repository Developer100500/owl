from camel.types import ModelPlatformType, ModelType

for name, member in ModelType.__members__.items():
    print(f"Name: {name}, Value: {member.value}")