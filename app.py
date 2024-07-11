import streamlit as st
import streamlit.components.v1 as cm
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Yassine-portfolio",
                   page_icon="🌍",
                   layout="wide")


page_bg_img = '''
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://media.istockphoto.com/id/1298523613/vector/abstract-white-and-light-gray-wave-modern-soft-luxury-texture-with-smooth-and-clean-vector.jpg?s=612x612&w=0&k=20&c=_6kcCxvGyEip9pDPygONXH1OoW7aNBuh899mwE2TQXI=");
background-size: cover;
}
[data-testid="stHeader"]{
background-color: rgba(0,0,0,0);


}

}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)




st.title("My Professional Portfolio")

# navigation
selection = option_menu(
        menu_title=None,
        options=['About me', 'Tableau Projects', 'Machine Learning Projects','Streamlit projects'],
        icons=['home','book','robot','bar'],
        orientation='horizontal'
    )


# CV section
if selection == 'About me':
    with open('cv.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

        # Display the HTML content in Streamlit
        cm.html(html_content, height=800, scrolling=True)

    
    
            




    
   

    
    


# Tableau Projects section
elif selection == 'Tableau Projects':
    st.title('Tableau Projects')
    
    # Embed Tableau visualization using iframe
    st.header("RH dashboard dashboard ",divider="blue")
    st.info('This is a comprehensive dashboard that informs us about the human resource structure of the IBM company by highlighting the employees distribution, age, working hours, social status, and satisfaction metrics. The role of this dashboard is to help HR managers make data-driven decisions to motivate the HR capital and establish suitable HR policies.')
    
    tableau_url = """<div class='tableauPlaceholder' id='viz1719329547341' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;IB&#47;IBMRHdashbord&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='IBMRHdashbord&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;IB&#47;IBMRHdashbord&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1719329547341');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='1900px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='1327px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='1900px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='1327px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='2377px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
                    """
    cm.html(tableau_url,width=1290,height=970)

    st.header("Adidas Sales dashboard ",divider="blue")
    st.info("We analyzed the Adidas sales dataset to understand sales performance by region, method, and product. Our analysis provided valuable insights into the company's financial performance")
    tableau_url="""<div class='tableauPlaceholder' id='viz1719331639378' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ad&#47;adidasdash&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='adidasdash&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ad&#47;adidasdash&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1719331639378');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1290px';vizElement.style.height='1027px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1290px';vizElement.style.height='1027px';} else { vizElement.style.width='100%';vizElement.style.height='2077px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script> """
    cm.html(tableau_url,width=1290,height=970)  

    st.header("Hotel dashboard ",divider="blue")
    st.write('..')
    tableau_url = """<div class='tableauPlaceholder' id='viz1719331892394' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ho&#47;HotelDashbord&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='HotelDashbord&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ho&#47;HotelDashbord&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1719331892394');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1877px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
    """
    cm.html(tableau_url,1290,height=970)

    st.header("Netflix dashboard",divider="blue")
    tableau_url="""<div class='tableauPlaceholder' id='viz1719332778892' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pr&#47;project3_16930826625850&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='project3_16930826625850&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pr&#47;project3_16930826625850&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1719332778892');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1290px';vizElement.style.height='927px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1290px';vizElement.style.height='927px';} else { vizElement.style.width='100%';vizElement.style.height='2227px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
    """
    cm.html(tableau_url,1290,height=900)

    
 

elif selection == 'Streamlit projects':
    st.subheader('Streamlit web app',divider="blue")
    video_file = open("sales_dash2.mp4",'rb')
    video_bytes = video_file.read()
    with st.container(border=True):
        col = st.columns(2)
        with col[0]:
            st.subheader("Sales dashboard")
            st.video(video_bytes)
    with col[1]:
            video_file = open("stock_vis.mp4",'rb')
            video_bytes= video_file.read() 
            st.subheader('stock visualizer')
            st.video(video_bytes)




















# Machine Learning Projects section
elif selection == 'Machine Learning Projects':
    st.title(' Machine Learning Projects')
    
    
    with st.container(border=True):
        col1,col2 = st.columns(2)
        with col1:
            st.subheader(' consumer behavior classification ')
            st.image('consumer.jpg')
            st.link_button('</>','https://github.com/YassineSdk/KNNclassifier_consumer-behavior-')
    
            st.subheader('insurrance price prediction')
            st.image("insurance.jpg")
            st.info("For this project, we are analyzing insurance data that includes information on whether an individual smokes or not, their sex, age, region, BMI, and the related insurance cost. Our main objective is to understand the relationship between the insurance cost and certain variables such as smoking habits, sex, age, region, and BMI ")
            st.link_button("</>","https://github.com/YassineSdk/medical-Insurance-Prediction")

            st.subheader("E-commerce model")
            st.image("eco.jpg")
            st.link_button('</>','https://github.com/YassineSdk/ecommerce_model-')
        with col2 :
            st.subheader('loans amortization c++')
            st.image("c++.jpg")
            st.link_button('</>','https://github.com/YassineSdk/loans-_amortization.cpp')

            st.subheader("Laptop pricing ")
            st.image("laptop.jpg")
            st.link_button('</>','https://github.com/YassineSdk/Laptop-Pricing-')


