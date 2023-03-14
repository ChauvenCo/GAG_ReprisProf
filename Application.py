class Application:
    def __init__(self, store, user, persist):
        self._store = store
        self._user = user
        self._persist = persist

    def save(self):
        self._persist.save(self)
