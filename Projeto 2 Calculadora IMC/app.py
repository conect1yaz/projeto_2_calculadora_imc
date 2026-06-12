import streamlit as st

#------------------------------------SIDEBAR
st.sidebar.title("Calculadora IMC")

st.sidebar.image("logo.png")

#------------------------------------BODY
st.title("Calculadora de IMC")
peso = st.text_input("Digite seu peso: ")
altura = st.text_input("Digite sua altura: ")

if st.button("Calcular"):
    peso = float(peso)
    altura = float(altura)

    imc = peso / (altura**2)

    if imc < 18.5:
        class_imc= "abaixo_peso"
        st.warning(f"Seu IMC é {imc:.2f}. Você está abaixo do peso")
        
    elif imc < 24.9:
        class_imc = "peso_saudavel"
        st.success(f"Seu IMC é {imc:.2f}. Você está com o peso ideal! ")

    elif imc < 29.9:
        class_imc = "sobrepeso"
        st.warning(f"Seu IMC é {imc:.2f}. Você está com sobrepeso")

    elif imc < 34.9:
        class_imc= "obesidade_1"
        st.warning(f"Seu IMC é {imc:.2f}. Você está com Obesidade Grau I")

    elif imc < 39.9:
        class_imc = "obesidade_2"
        st.error(f"Seu IMC é {imc:.2f}. Você está com Obesidade Grau II")

    else:
        class_imc= "obesidade_3"
        st.error(f"Seu IMC é {imc:.2f}. Você está com Obesidade Grau III")


    st.markdown("---")

    with open(f"{class_imc}.txt", "r", encoding='utf-8') as f:
        conteudo = f.read()

        st.image(f"{class_imc}.png")
        st.markdown(conteudo)