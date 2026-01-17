import streamlit as st

st.set_page_config(page_title="Climate Awareness Chatbot", page_icon="🌍")
st.title("🌍 Climate Awareness Chatbot")
st.write("Ask me any question related to climate, environment, or sustainability.")

def get_response(user_input):
    user_input = user_input.lower()

    if "climate change" in user_input:
        return "Climate change refers to long-term changes in temperature and weather patterns, mainly caused by human activities such as burning fossil fuels.Climate change causes rising sea levels, extreme weather events, melting glaciers, droughts, floods, heatwaves, and loss of biodiversity.Individuals can reduce climate change by saving energy, using public transport, reducing waste, recycling, planting trees, and adopting sustainable lifestyles."

    elif "global warming" in user_input:
        return "Global warming is the gradual increase in Earth's average temperature due to greenhouse gas emissions.Global warming alters climate patterns, leading to changes in rainfall, increased temperatures, and more frequent extreme weather events.Global warming causes melting glaciers, rising sea levels, heatwaves, droughts, stronger storms, and damage to ecosystems.Global warming can be reduced by using renewable energy, improving energy efficiency, reducing deforestation, and limiting greenhouse gas emissions."

    elif "greenhouse" in user_input:
        return "The greenhouse effect occurs when gases trap heat in Earth's atmosphere, leading to warming.Greenhouse gases are gases such as carbon dioxide, methane, nitrous oxide, and water vapor that trap heat in Earth’s atmosphere.Burning fossil fuels, deforestation, industrial activities, and intensive agriculture increase greenhouse gas emissions.The greenhouse effect can be reduced by lowering greenhouse gas emissions, using renewable energy, improving energy efficiency, and protecting forests."

    elif "carbon footprint" in user_input:
        return "A carbon footprint is the total amount of greenhouse gases produced by human activities. You can reduce it by saving energy, using public transport, and reducing waste.Carbon footprints are caused by activities such as electricity usage, transportation, industrial processes, food consumption, and waste generation.The main sources include burning fossil fuels, transportation, electricity production, agriculture, and manufacturing.A higher carbon footprint increases greenhouse gas concentrations, contributing to global warming and climate change.Individuals can reduce their carbon footprint by saving energy, using public transport, reducing waste, recycling, and adopting sustainable lifestyles."

    elif "renewable" in user_input or "solar" in user_input or "wind" in user_input:
        return "Renewable energy comes from natural sources like solar, wind, and hydro power that are continuously replenished.Renewable energy produces little or no greenhouse gases, reducing carbon emissions and slowing global warming.Renewable energy supports sustainable development by providing clean energy, reducing emissions, and promoting economic growth.Renewable energy is important because it reduces greenhouse gas emissions, decreases dependence on fossil fuels, and helps combat climate change."

    elif "deforestation" in user_input:
        return "Deforestation is the large-scale clearing or cutting down of forests, often to make land available for agriculture, urban development, or industrial use.Deforestation increases carbon dioxide levels and reduces biodiversity, contributing to climate change.The main causes include agricultural expansion, logging, urbanization, mining, and infrastructure development.Deforestation affects humans by causing climate instability, reducing water availability, increasing natural disasters, and affecting livelihoods.Deforestation can be prevented through afforestation, sustainable forestry, conservation policies, and reducing paper and wood consumption."

    elif "plastic" in user_input or "waste" in user_input:
        return "Plastic waste is a serious problem because it takes hundreds of years to decompose, harms wildlife, and pollutes ecosystems.The main sources include single-use plastics such as bags, bottles, packaging materials, and disposable items.Reducing plastic use, recycling, and proper waste management help protect the environment.Waste management is the process of collecting, treating, recycling, and disposing of waste in an environmentally safe manner.The 3Rs stand for Reduce, Reuse, and Recycle, which help minimize waste and protect the environment."

    elif "effects" in user_input:
        return "Climate change causes rising sea levels, extreme weather, droughts, floods, and loss of biodiversity.Climate change disrupts ecosystems by altering habitats, affecting food chains, and increasing the risk of species extinction.Climate change leads to water scarcity in some regions and floods in others due to changes in rainfall and melting glaciers.Climate change increases health risks such as heat-related illnesses, spread of infectious diseases, malnutrition, and respiratory problems.Climate change intensifies natural disasters by increasing energy in the atmosphere, leading to stronger storms and extreme events."

    elif "solution" in user_input or "prevent" in user_input:
        return "Climate change can be prevented or reduced by cutting fossil fuel use, improving energy efficiency, adopting clean energy, and increasing environmental awareness.Solutions include using renewable energy, conserving resources, planting trees, and spreading awareness.Individuals can help by saving electricity, using public transport, reducing waste, recycling, planting trees, and adopting eco-friendly lifestyles.Proper waste management reduces methane emissions from landfills and lowers pollution and greenhouse gas release.Forests absorb carbon dioxide from the atmosphere and help regulate climate, making forest conservation essential."

    else:
        return (
            "🌱 This is a climate awareness chatbot. "
            "You can ask about climate change, global warming, renewable energy, pollution, sustainability, "
            "carbon footprint, or environmental protection."
        )

user_input = st.text_input("💬 Ask your question:")

if user_input:
    st.success(get_response(user_input))

st.markdown("---")
st.caption("EcoBot – Climate Awareness Chatbot")
