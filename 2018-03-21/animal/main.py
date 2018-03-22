import cat
import dog
import fox
import pom
import shepherd


animals = [
    cat.Cat('Garfield'),
    dog.Dog('Odie'),
    pom.Pom('Miley'),
    shepherd.Shepherd('General'),
    fox.Fox('Nick P Wilde')
]

for animal in animals:
    print(animal.get_name() + ', ' + animal.speak())
