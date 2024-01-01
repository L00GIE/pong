class Scene:

    def __init__(self):
        self.objects = []

    def loop(self):
        for obj in self.objects:
            if hasattr(obj, "loop"):
                obj.loop()

    def add(self, obj):
        self.objects.append(obj)

    def remove(self, obj):
        if obj in self.objects:
            self.objects.remove(obj)