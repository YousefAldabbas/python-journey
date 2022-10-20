class Luxury:
    watches_created = 0

    def __init__(self):
        self.watches_created += 1

    def get_number_of_watches_created(self):
        return self.watches_created

    @classmethod
    def watch_with_engraving(cls, engraving):
        watch = cls()
        watch.engraving = engraving
        return watch

    def validation(self):
        pass


inc = Luxury()