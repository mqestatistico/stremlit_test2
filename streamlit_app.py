import pandas as pd
import streamlit as st


def display_introduction():
    """ Mostrando como usar o Stramlit"""
    st.title("Introdução ao Streamlit")
    st.text(
        """O Stramlit permite escrever aplições 
        simpleamente chamando funções""")
    st

def display_text() :
    """Formas de mostrar texto"""
    st.header("1.) Como mostrar texto")
    st.subheader("1.1 Este é um subcabecalho")
    st.markdown(" _Markdown_")
    st.latex(r"e^{i/pi} + 1 = 0")
    st.write("O write aceita qualquer coisa que vc jogar")
    st.write([1,2,3,4,5,6,7,8,9,0])
    st.write({1,2,3,4,5,6})
    code= """
        for i in range(10):
            print(i)
    """
   
    st.code(body = code, language="python")
    


def display_magig_functions():
    """Mostra textos de forma mágica"""
    
    a = "Este texto será exibido de forma mágica pelo streamli"
    a
    """O Streamlit consegue exibir strings formatadas"""
    b = pd.DataFrame({
        "cola": [1, 2, 3],
        "cola b": [4, 5, 6]       
    })
    b
    """---"""
    st.title("Formas de titulos:")
    "# Titulo de nivel 1"
    "## Titulo de nivel 2"
    "### Titulo de nivel 3"
    "#### Titulo de nivel 4"
    "##### Titulo de nivel 5"
    "###### Titulo de nivel 6"
    
def display_data():
    """Formas de mostrar dados pelo Streamli"""
    b = pd.DataFrame({
            "cola": [1, 2, 3],
            "cola b": [4, 5, 6]       
        })
    "#### Usando dataframe"
    st.dataframe(b)
    
    "#### Usando tabelas"
    st.table(b)

    "#### Usando o dicionário"
    st.json(b.to_dict())
    
    "#### Usando Json"
    st.json(b.to_json())
    
    "#### Mostrando métricas"
    st.metric(
         label ="Temperatura" ,
         value = "30 g C",
         delta = "3 g C",
         delta_color="normal"                
              )
    st.metric(
         label ="Umidade" ,
         value = "30%",
         delta = "5%",
         delta_color="inverse"                
              )
    
def display_midia():    
    """Formas de mostrar midia"""
    """#### Mostrando audio"""
    st.audio("https://ssl.gstatic.com/dictionary/static/sounds/oxford/morning--_us_1.mp3")
    
    """#### Mostrando imagens"""
    st.image("https://s3.amazonaws.com/media.wikiaves.com.br/images/0024/4200668_606a27cf043bfb0d204f717f3c8be5e8.jpg")
    
    """#### Mostrando vídeos"""
    st.video("https://youtu.be/EUu7EhnDlss")
    
    
def display_columns():
    """Mostrando valores em colunas"""    
    """#### Mostrando objetos em colunas"""
    col1, col2, col3 = st.columns([1, 1, 1]) #parametros é ou numero de colunas ou uma lista com os tamanhos das colunas
    col1.image("https://s3.amazonaws.com/media.wikiaves.com.br/images/0024/4200668_606a27cf043bfb0d204f717f3c8be5e8.jpg")
    col2.audio("https://ssl.gstatic.com/dictionary/static/sounds/oxford/morning--_us_1.mp3")
    col3.video("https://youtu.be/EUu7EhnDlss")
    
    st.write("Esta sentençã não irá aparecem em nunhuma columa")
    col1.write("Já esta sentença aparecerá somente na coluna 1")
    
    with col2:
        st.write("Este texto vai estar na coluna 2 apenas")
        
        

def display_status():
    """Mostra as formas de status"""
    
    st.error("ERRO: A sua opeação deu errado! Fique atento.")
    
    st.warning("Advertência: Fique esperto!!!")
    
    st.info("Informação: Isso é uma informação.")
    
    st.success("""SUCESSO: Essa é uma mensagem de sucesso
               
               Continuação da mensagem de sucesso""")
    
    try:
        st.write(10/0)
    except ZeroDivisionError as error:
        st.exception(error)    


def display_widgets():
    """Formas de widgets do streamlit"""
    """#### Mostrando widgets"""
    """#### Botões clicáveis"""
    button = st.button("Clique aqui")
    button
    
    """#### Checkbox"""
    button = st.checkbox("Eu concordo, clique aqui.")
    button
    
    """### Radio button"""
    radio = st.radio("Selecione a opção", ["Gatos","Cachorros", "Calopsitas"])    
    radio
    
    """### Selectbox"""
    selectbox = st.selectbox("Selecione a opção", ["Gatos","Cachorros", "Calopsitas"])    
    selectbox
    
    """### Selectslider"""
    selectslider = st.select_slider("Selecione a opção", ["Gatos","Cachorros", "Calopsitas"])    
    selectslider
   
    """#### Selec number"""
    number = st.number_input("selecione um número de 0 a 10", 0,10)
    number

    """#### imput Text values"""
    area = st.text_area("Entre com um texto qulquer:")
    area

    """### Selecione uma data"""
    data = st.date_input("Qual é a data:")
    data
    
    """### Selecione um horário:"""
    horario = st.time_input("Qual é o horario")
    horario
    
    """### Selecionando arquivo para upload"""
    upload = st.file_uploader("Entre com o arquivo")
    upload
    
    """### Clique no botão para baixar o CSV"""
    data = pd.DataFrame({
            "cola": [1, 2, 3],
            "cola b": [4, 5, 6]       
        })
    st.write(data)
    csv=data.to_csv(index=False)
    download = st.download_button("Download arquivo docx", csv)
    
def display_sidebar() :
    """Mostra uma barra lateral"""
    with st.sidebar:
        st.title("Navegação ou tutorial")
        
        opcoes = {
            "Introdução": display_introduction,
            "Formas de mostrar texto": display_text,
            "Forms mágicas": display_magig_functions,
            "Mostrando dados":display_data,
            "Mostrando midia":display_midia,
            "Mostrando valores em colunas": display_columns,
            "Mostrando Status":display_status,
            "Widgets são esses": display_widgets
        }
        opt = st.radio("Selecione a opção de navegação", opcoes)
        
        st.write(opt)
    opcoes[opt]()

display_sidebar()

