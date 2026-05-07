class Arxitektor:
    def __init__(self, ism, familiya, tajriba):
        self.ism = ism
        self.familiya = familiya
        self.tajriba = tajriba

    @classmethod
    def yarat(cls, ism, familiya, tajriba):
        return cls(ism, familiya, tajriba)

    def info(self):
        return f"Ism: {self.ism}, Familiya: {self.familiya}, Tajriba: {self.tajriba} yil"

arxitektor = Arxitektor.yarat("Ali", "Valiyev", 10)
print(arxitektor.info())
```

Kodda `@classmethod` dekoratori `yarat` metodi uchun ishlatilgan. Ushbu metod klassga tegishli bo'lib, klassning nusxasini qaytaradi. `yarat` metodi klassga tegishli bo'lishi uchun `cls` so'zidan foydalanilgan. `cls` klassning nomi bo'lib, klassga tegishli metodlarda ishlatiladi.
