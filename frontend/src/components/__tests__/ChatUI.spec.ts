import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import ChatUI from '../ChatUI.vue'

describe('ChatUI', () => {
  it('renders properly', () => {
    const wrapper = mount(ChatUI, { props: { msg: 'Story Chatbot' } })
    expect(wrapper.text()).toContain('Story Chatbot')
  })
})
