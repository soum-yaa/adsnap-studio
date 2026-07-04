import streamlit as st
from services.ad_copy import generate_ad_copy, build_image_prompt

st.set_page_config(
    page_title="AdSnap AI Creative Studio",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    st.title("🎨 AdSnap AI Creative Studio")
    st.markdown(
        "Generate product ad concepts, marketing copy, CTAs, hashtags, and AI image prompts for social media campaigns."
    )

    tab1, tab2, tab3 = st.tabs([
        "✨ Ad Concept Generator",
        "🧠 Prompt Builder",
        "📌 Project Info"
    ])

    with tab1:
        st.header("✨ Generate Ad Concept")

        col1, col2 = st.columns([2, 1])

        with col1:
            product_name = st.text_input("Product Name", placeholder="Example: Smart Water Bottle")
            product_description = st.text_area(
                "Product Description",
                placeholder="Describe the product, features, benefits, or target use case..."
            )
            audience = st.text_input("Target Audience", value="young professionals")

        with col2:
            tone = st.selectbox("Ad Tone", ["Premium", "Minimal", "Bold", "Luxury", "Playful"])
            platform = st.selectbox("Platform", ["Instagram", "LinkedIn", "Facebook", "Website"])
            campaign_goal = st.selectbox(
                "Campaign Goal",
                ["Brand Awareness", "Product Launch", "Sales Conversion", "Engagement"]
            )

        if st.button("🚀 Generate Ad Concept", type="primary"):
            if not product_name:
                st.warning("Please enter a product name.")
            else:
                copy = generate_ad_copy(product_name, audience, tone, platform)
                prompt = build_image_prompt(product_name, audience, tone, platform)

                st.success("Ad concept generated successfully!")

                st.subheader("📢 Generated Ad Copy")
                st.markdown(f"**Headline:** {copy['headline']}")
                st.markdown(f"**Caption:** {copy['caption']}")
                st.markdown(f"**CTA:** {copy['cta']}")
                st.markdown(f"**Hashtags:** {copy['hashtags']}")

                st.subheader("🎨 AI Image Generation Prompt")
                st.code(prompt, language="text")

                st.subheader("📦 Campaign Summary")
                st.write({
                    "Product": product_name,
                    "Audience": audience,
                    "Tone": tone,
                    "Platform": platform,
                    "Goal": campaign_goal
                })

    with tab2:
        st.header("🧠 AI Prompt Builder")

        product = st.text_input("Product", key="prompt_product", placeholder="Example: Wireless headphones")
        scene = st.text_input("Scene / Background", placeholder="Example: modern desk setup")
        style = st.selectbox("Visual Style", ["Realistic", "Luxury", "Minimal", "Futuristic", "Vibrant"])
        lighting = st.selectbox("Lighting", ["Studio lighting", "Natural light", "Soft shadows", "Cinematic lighting"])
        aspect_ratio = st.selectbox("Aspect Ratio", ["1:1", "16:9", "9:16", "4:3"])

        if st.button("✨ Build Prompt"):
            if not product:
                st.warning("Please enter a product.")
            else:
                final_prompt = (
                    f"Professional advertisement image of {product}, "
                    f"placed in {scene if scene else 'a clean premium background'}, "
                    f"{style.lower()} visual style, {lighting.lower()}, "
                    f"high-resolution product photography, modern commercial ad, "
                    f"aspect ratio {aspect_ratio}"
                )

                st.subheader("Generated Prompt")
                st.code(final_prompt, language="text")

    with tab3:
        st.header("📌 About This Project")

        st.markdown("""
        **AdSnap AI Creative Studio** is a GenAI-powered marketing assistant that helps users create:
        
        - Product ad concepts
        - Marketing headlines
        - Captions and CTAs
        - Hashtags
        - AI image generation prompts
        - Platform-specific campaign ideas
        
        This version is deployment-ready and does not require a paid image-generation API key.
        """)

        st.subheader("🛠️ Tech Stack")
        st.markdown("""
        - Python
        - Streamlit
        - Prompt Engineering
        - Modular service-based architecture
        """)

        st.subheader("🚀 Future Scope")
        st.markdown("""
        - Add OpenAI/Gemini integration
        - Generate actual ad images
        - Add brand color extraction
        - Export ads as PNG/PDF
        - Save campaign history
        """)

if __name__ == "__main__":
    main()