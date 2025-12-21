import type { Directive } from "vue"

export const focusSlash: Directive = {
  mounted(el) {
    const handler = (e: KeyboardEvent) => {
      if (e.key === "/" && document.activeElement === document.body) {
        e.preventDefault()
        el.focus()
      }
    }

    window.addEventListener("keydown", handler)
    el._slashHandler = handler
  },
  unmounted(el) {
    window.removeEventListener("keydown", el._slashHandler)
  }
}
