"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx
from constants import *
from passwordgenerator.states.states import PasswordGeneratorState, LanguageSelectState

def index() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.link(rx.image(src="jddevlogo.webp"), href="/", is_external=False, class_name="logo-link"),
                rx.box(
                    rx.hstack(
                        rx.link("Github", href=GITHUB, is_external=True, class_name="navbar-link"),
                        rx.link("Portfolio", href="/", is_external=True, class_name="navbar-link"),
                        rx.link("X/Twitter", href=TWITTER, is_external=True, class_name="navbar-link"),
                        rx.link("Ko-Fi", href=KOFI, is_external=True, class_name="navbar-link"),
                        rx.drawer.root(
                        rx.drawer.trigger(rx.button(rx.icon("menu"),class_name="mobile-menu-button")),
                        rx.drawer.overlay(z_index="5"),
                        rx.drawer.portal(
                        rx.drawer.content(
                        rx.box(
                        rx.drawer.close(rx.box(rx.button(rx.icon("menu"),class_name="mobile-menu-button-close")),),
                        rx.flex(rx.link("Github", href=GITHUB, is_external=True, class_name="phone-navbar-link"),
                        rx.link("Portfolio", href="/", is_external=True, class_name="phone-navbar-link"),
                        rx.link("X/Twitter", href=TWITTER, is_external=True, class_name="phone-navbar-link"),
                        rx.link("Ko-Fi", href=KOFI, is_external=True, class_name="phone-navbar-link"),
                            direction="column",
                            class_name="links-drawer"
                        )),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="40%",
                        padding="2em",
                        class_name="drawer-container"
                        # background_color=rx.color("green", 3)
        ),
    ),
    direction="left",
),
                        rx.button(rx.text(LanguageSelectState.change_language_text, class_name="language-text"), on_click=lambda: LanguageSelectState.toggle_language, class_name="language-button"),
                        class_name="links-container" 
                    ),
                    class_name="navbar-container",  
                ),
                class_name="navbar-container"
            ),
            rx.box(
                rx.vstack(
                    rx.heading(LanguageSelectState.heading_text, class_name="title-heading"),
                    rx.box(rx.text(PasswordGeneratorState.generated_password, class_name="password-text"), class_name="text-container"),
                    rx.text(LanguageSelectState.help_text, class_name="help-text"),
                            rx.box(
                rx.hstack(
                    rx.button(LanguageSelectState.eight_button_text, on_click=lambda: PasswordGeneratorState.on_button_click(8), class_name="character-button"),
                    rx.button(LanguageSelectState.thirteen_button_text, on_click=lambda: PasswordGeneratorState.on_button_click(13), class_name="character-button"),
                    rx.button(LanguageSelectState.sixteen_button_text, on_click=lambda: PasswordGeneratorState.on_button_click(16), class_name="character-button"),
                    class_name="password-gen-button-container"
                    )
                ),class_name="password-gen-stack",
                ),
                class_name="password-gen-box"
                
            ),
            rx.box(rx.text(LanguageSelectState.footer_text, class_name="footer-text"),class_name="footer-container"),
            class_name="stack-container"),
        class_name="main-container"
    )

app = rx.App(stylesheets=["styles.css", "https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,100..900;1,100..900&family=Kanit:ital@0;1&family=League+Spartan:wght@100..900&display=swap"])
app.add_page(index)
