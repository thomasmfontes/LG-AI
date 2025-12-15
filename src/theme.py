from __future__ import annotations
from typing import Iterable
import gradio as gr
from gradio.themes.base import Base
from gradio.themes.utils import colors, fonts, sizes

class LGTheme(Base):
    def __init__(
        self,
        *,
        primary_hue: colors.Color | str = colors.red,
        secondary_hue: colors.Color | str = colors.neutral,
        neutral_hue: colors.Color | str = colors.neutral,
        spacing_size: sizes.Size | str = sizes.spacing_md,
        radius_size: sizes.Size | str = sizes.radius_lg,
        text_size: sizes.Size | str = sizes.text_lg,
        font: fonts.Font | str | Iterable[fonts.Font | str] = (
            fonts.GoogleFont("Inter"),
            "ui-sans-serif",
            "system-ui",
            "sans-serif",
        ),
        font_mono: fonts.Font | str | Iterable[fonts.Font | str] = (
            fonts.GoogleFont("IBM Plex Mono"),
            "ui-monospace",
            "Consolas",
            "monospace",
        ),
    ):
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
            font=font,
            font_mono=font_mono,
        )
        
        # LG Brand Colors override
        # LG Red: #A50034
        # We approximate the palette around this color for primary actions
        self.set(
            # Page background
            body_background_fill="var(--background-fill-primary)",
            body_background_fill_dark="#121212",
            
            # Primary Button (LG Red)
            button_primary_background_fill="#A50034",
            button_primary_background_fill_hover="#8a002b",
            button_primary_text_color="white",
            button_primary_border_color="#A50034",
            
            # Cards / Containers
            block_background_fill="white",
            block_background_fill_dark="#1e1e1e",
            block_label_text_size="*text_sm",
            block_title_text_weight="600",
            
            # Input Fields
            input_background_fill="#f9fafb",
            input_background_fill_dark="#2b2b2b",
            input_border_color_focus="#A50034",
            
            # Borders & Radius
            block_radius="12px",
            container_radius="12px",
            button_large_radius="50px", # Pill shape for main actions
        )
