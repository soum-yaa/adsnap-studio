def generate_ad_copy(product_name, audience, tone, platform):
    headline = f"{product_name} made for {audience}"
    caption = (
        f"Discover {product_name}, designed for {audience}. "
        f"With a {tone.lower()} style, this ad is perfect for {platform} campaigns."
    )
    cta = "Shop Now" if platform in ["Instagram", "Facebook"] else "Learn More"

    return {
        "headline": headline,
        "caption": caption,
        "cta": cta,
        "hashtags": f"#{product_name.replace(' ', '')} #AIAds #Marketing"
    }


def build_image_prompt(product_name, audience, tone, platform):
    return (
        f"Professional product advertisement for {product_name}, "
        f"targeted at {audience}, {tone.lower()} mood, "
        f"high-quality studio lighting, clean background, "
        f"modern social media ad for {platform}, premium commercial photography"
    )