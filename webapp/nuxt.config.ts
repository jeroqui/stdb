// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    modules: [
        '@nuxtjs/tailwindcss',
        '@pinia/nuxt',
        'nuxt-icon',
        '@nuxtjs/apollo',
    ],

    apollo: {
        clients: {
            default: {
                httpEndpoint: 'http://127.0.0.1:8000/graphql/'
            }
        },
    },
})
