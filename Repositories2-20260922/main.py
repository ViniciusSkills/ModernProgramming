from app_data import AppData
from abstract_demo import Dog, Cat, LandBird, FlyBird, Dinosaur
from heroes import HumanHero, Batman, Superman
from payment import Pix, CreditCard, DebitCard


print(AppData.APP_VERSION)

dog = Dog("Alfie")
cat = Cat("Bianca")
dog1 = Dog("Fido")
dinosaur = Dinosaur("Caramelo")

brian = LandBird("Brian")
fly_bird = FlyBird("Sky")

print(f"Dog: {dog.describe()}")
print(f"Cat: {cat.describe()}")
print(f"Bird: {brian.describe()}")
print(f"Brian Jumps: {brian.jump()}")
print(f"Sky Jumps: {fly_bird.jump()}")
print(f"Cat Jumps: {cat.jump()}")
print(f"Dinosaur: {dinosaur.describe()}")

human_hero = HumanHero()

batman = Batman()
superman = Superman()

batman.fly()
batman.land()
superman.force()

pix = Pix("Vinicius")
credit_card = CreditCard("Marcelo")
debit_card = DebitCard("Ozzy")

print(pix.describe())
print(credit_card.describe())
print(debit_card.describe())