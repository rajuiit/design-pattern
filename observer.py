class NewsPublisher:
    def __init__(self):
        self.subscribers = []  # List of observers

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify_subscribers(self, news):
        for subscriber in self.subscribers:
            subscriber.update(news)
class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, news):
        print(f"{self.name} received news: {news}")
if __name__ == "__main__":
    # Create the subject
    news_publisher = NewsPublisher()

    # Create subscribers
    subscriber1 = Subscriber("Alice")
    subscriber2 = Subscriber("Bob")
    subscriber3 = Subscriber("Charlie")

    # Subscribe to the news publisher
    news_publisher.subscribe(subscriber1)
    news_publisher.subscribe(subscriber2)

    # Publish news
    news_publisher.notify_subscribers("Breaking News: Observer Pattern Explained!")

    # Unsubscribe a subscriber
    news_publisher.unsubscribe(subscriber1)

    # Publish another news update
    news_publisher.notify_subscribers("Latest Update: Design Patterns Made Easy!")
