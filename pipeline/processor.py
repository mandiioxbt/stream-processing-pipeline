class StreamProcessor:
    def __init__(self, topic, group): self.topic, self.group, self.offsets = topic, group, {}
    def process(self, handler):
        for msg in self.poll():
            try: handler(msg); self.commit(msg.offset)
            except: self.retry(msg)
    def poll(self): return []
    def commit(self, offset): self.offsets[self.topic] = offset
