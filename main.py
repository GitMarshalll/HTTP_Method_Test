import requests
#yangi o'zgarish
BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def get_posts():
    response = requests.get(BASE_URL)
    print("GET Status:", response.status_code)
    print("Response JSON:", response.json()[:2])  # faqat 2 ta element ko‘rsatadi

def create_post():
    data = {
        "title": "Test Post",
        "body": "Bu test posti",
        "userId": 1
    }
    response = requests.post(BASE_URL, json=data)
    print("POST Status:", response.status_code)
    print("Response JSON:", response.json())

def update_post(post_id):
    data = {
        "id": post_id,
        "title": "Yangilangan sarlavha",
        "body": "Yangilangan post matni",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/{post_id}", json=data)
    print("PUT Status:", response.status_code)
    print("Response JSON:", response.json())

def delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/{post_id}")
    print("DELETE Status:", response.status_code)
    if response.status_code == 200:
        print(f"Post ID {post_id} muvaffaqiyatli o‘chirildi.")
    else:
        print("O‘chirishda xatolik yuz berdi.")

def main():
    while True:
        print("\nHTTP metodlarini test qilish menyusi:")
        print("1. GET - Postlar ro‘yxatini olish")
        print("2. POST - Yangi post yaratish")
        print("3. PUT - Postni yangilash")
        print("4. DELETE - Postni o‘chirish")
        print("5. Chiqish")

        choice = input("Tanlovingizni kiriting (1-5): ")

        if choice == "1":
            get_posts()
        elif choice == "2":
            create_post()
        elif choice == "3":
            post_id = input("Yangilamoqchi bo‘lgan post ID sini kiriting: ")
            update_post(post_id)
        elif choice == "4":
            post_id = input("O‘chirmoqchi bo‘lgan post ID sini kiriting: ")
            delete_post(post_id)
        elif choice == "5":
            print("Dasturdan chiqildi.")
            break
        else:
            print("Noto‘g‘ri tanlov. Iltimos, qaytadan urinib ko‘ring.")

if __name__ == "__main__":
    main()