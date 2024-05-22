# 🌸 Scentiment Chatbot 🌸

Welcome to the Scentiment Chatbot repository! This project showcases an AI-powered assistant built using the ReAct (Reason and Action) technique. We utilize built-in functions to seamlessly handle customer queries related to orders, product recommendations, and discounts for Scentiment products.. The chatbot leverages OpenAI's GPT model and Chainlit for seamless message handling.

## 📚 Table of Contents

- [🚀 Installation](#installation)
- [💻 Usage](#usage)
- [✨ Features](#features)
- [💬 Example Queries](#example-queries)

## 🚀 Installation

- **📦 Order Support**: Retrieve comprehensive information about customer orders, including shipping status, cancellations, and more.
- **🏅 Product Recommendations**: Offer personalized product recommendations tailored to customer preferences and needs.
- **💸 Discount Offers**: Inform customers about ongoing discounts, promotions, and special offers.
- **🤗 Friendly Assistance**: Patrick, a friendly and neutral support entity, is here to help with any inquiries.


1. **Clone the repository:**

   ```bash
   git clone https://github.com/RaghavK24/Scentiment-Chatbot.git
   cd Scentiment
   ```
2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

1. **Run the Chainlit application:**

   ```bash
   chainlit run new_chat.py
   ```
2. **Interact with the chatbot** through the Chainlit interface. You can ask about:

   - 📦 **Order details**
   - 🕯️ **Product recommendations**
   - 💸 **Current discounts**

## ✨ Features

- **Order Details**: 📦 Retrieve all information about customer orders, including shipping status, cancellations, and estimated delivery dates.
- **Product Recommendations**: 🕯️ Provide personalized product recommendations based on the type of product the user is interested in.
- **Discount Offers**: 💸 Inform users about current discount offers and promotions.

## 💬 Example Queries

- **Order Details**: "Can you tell me the status of my order with ID 12345?" 📦
- **Product Recommendations**: "What diffusers do you recommend?" 🕯️
- **Discount Offers**: "Are there any discounts available right now?" 💸

---

Happy chatting! 🌟
