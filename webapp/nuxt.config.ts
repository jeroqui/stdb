// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    components: true,
    modules: [
        '@nuxtjs/tailwindcss',
        '@pinia/nuxt',
        'nuxt-icon',
        '@nuxtjs/apollo',
        '@blokwise/dynamic',
    ],

    apollo: {
        clients: {
            default: {
                httpEndpoint: 'http://127.0.0.1:8000/graphql/'
            }
        },
    },
})
