import matplotlib.pyplot as plt
import numpy as np

# Palette display functions
def display_palette(palette):
    n_colors = len(palette)
    fig, ax = plt.subplots(figsize=(n_colors, 2))
    
    for i, color in enumerate(palette):
        circle = plt.Circle((i * 0.8 + 0.5, 1), 0.5, color=color)
        ax.add_patch(circle)
        
    ax.set_xlim(0, n_colors * 0.8 + 0.2)
    ax.set_ylim(0, 2)
    
    ax.set_aspect('equal')
    ax.axis('off')
    plt.show()

def display_palettes(palettes):
    max_colors = max(len(palette) for palette in palettes.values())
    rows = len(palettes)
    
    fig, axes = plt.subplots(rows, 2, figsize=(5, 1 * rows), 
                             gridspec_kw={'width_ratios': [0.1, 4.9]})  # Make the first column very narrow
    
    for i, (palette_name, palette) in enumerate(palettes.items()):
        # Set the title in the first column
        axes[i, 0].text(0.5, 0.5, palette_name, va='center', ha='center', fontsize=12, fontname='DejaVu Serif')
        axes[i, 0].axis('off')

        # Display the color palette in the second column
        ax = axes[i, 1]
        n_colors = len(palette)
        
        for j, color in enumerate(palette):
            circle = plt.Circle((j * 0.8 + 0.5, 0.5), 0.5, color=color)
            ax.add_patch(circle)

        ax.set_xlim(0, max_colors * 0.8 + 0.2)  # Set the same x-axis limits for all
        ax.set_ylim(-0.1, 1.1)
        ax.set_aspect('equal')
        ax.axis('off')

    plt.tight_layout(pad=2.0)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.05)
    plt.show()
    
# Palettes


## Burke
burke = ["#a9bed9","#a6714a","#edab61","#fdf3a8", "#f6f2ea", "#b64434", "#613a24"]
burke_cool = ["#43403c", "#3c485f","#6485a4", "#a9bed9","#92a6b4"]
burke_warm = ["#613a24","#b64434","#f0734c","#fbe3b7","#fbffbe"]
burke_palettes = {'burke': burke, 'burke_cool': burke_cool, 'burke_warm': burke_warm}

## Yale-NUS
yalenus = ["#4b5328", "#9ccf5a", "#d1dfaa", "#929668", "#699328", "#6b706f", "#b47c5f", "#7cd2cd"]
yalenus_lib = ["#402316", "#937d68", "#c9c6bb", "#6c4027", "#bb552e", "#ffee9e"]
yalenus_palettes = {'yalenus': yalenus, 'yalenus_lib': yalenus_lib}

## NUS Bukit Timah
nusbtc = ["#a5acf3", "#e7a3e5", "#c0d4e2","#6c7cb4", "#d8cfbc", "#81334a","#f9e8b6","#5d6442"]
nusbtc_sunny = ["#124484","#b0dcf6","#8b98a0","#d3dfdc","#67852d","#c1d95d","#75524c","#f2a086"]
nusbtc = {'nusbtc':nusbtc, "nusbtc_sunny": nusbtc_sunny}

## Oxford
highstreet = ["#3a312d","#d9c8bd","#a69183","#b7bdcf","#706e79","#d61621", "#afc5f6", "#f7d5af"]
radcliffecamera=["#161a19","#ae9b7a","#e8d3a6","#b48f59","#a2c1e6","#6fbffe","#7d9ac3","#d5dee5","#656d38"]
bodleian = ["#d8ab75","#41291a","#956f4d","#a5abab","#6a605f","#ba262f","#fff188","#fefce5"]

oxford = {'highstreet':highstreet, 'radcliffecamera':radcliffecamera, 'bodleian':bodleian}

## Uni Themes

columbia_theme = ["#accce6", "#75aadb", "#003373", "#fcd450", "#cdc9c5", "#5e514e"]
oxford_theme = ["#002147","#a79d96","#f3f1ee","#122f53","#be0f34", "#f5cf47"]
nus_theme = ["#d97300", "#003882","#89734c", "#908d8d"]
uni_themes = {'columbia': columbia_theme, "oxford": oxford_theme, "nus": nus_theme}