class CountingClass:

    instance_created = 0

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.number = cls.instance_created
        cls.instance_created += 1
        return instance

    def __init__(self, value):
        self.value = value

if __name__ == "__main__":
    print("<<< створення екземпляру класу >>>")
    print(CountingClass.instance_created)



