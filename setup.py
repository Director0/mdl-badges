"""Подставляет ваш GitHub-ник и почту в JSON-файлы значка.

Запуск из папки badges:
    python setup.py ВАШ_НИК ваша@почта.ru

Почта должна совпадать с той, на которую зарегистрирован аккаунт Badgr.
В assertion попадёт только её SHA-256 хеш, сама почта не публикуется
(кроме поля email издателя в issuer.json, там можно указать любую контактную).
"""
import hashlib
import pathlib
import sys

if len(sys.argv) != 3:
    sys.exit("Использование: python setup.py ВАШ_НИК ваша@почта.ru")

username, email = sys.argv[1].strip(), sys.argv[2].strip().lower()
email_hash = hashlib.sha256(email.encode("utf-8")).hexdigest()

root = pathlib.Path(__file__).parent
for path in root.rglob("*.json"):
    text = path.read_text(encoding="utf-8")
    text = (text.replace("USERNAME", username)
                .replace("HASH", email_hash)
                .replace("EMAIL", email))
    path.write_text(text, encoding="utf-8")
    print("готово:", path.relative_to(root))

print("\nСсылка для Badgr:")
print(f"https://{username}.github.io/mdl-badges/assertions/1.json")
