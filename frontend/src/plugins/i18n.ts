import { createI18n } from 'vue-i18n';
import messages from '@intlify/unplugin-vue-i18n/messages'

export const i18n = createI18n({
    legacy: false,
    globalInjection: true,
    locale: window.navigator.language.substring(0, 2) || 'en',
    fallbackLocale: 'en',
    availableLocales: ['en', 'es', 'pt'],
    messages: messages,
});
