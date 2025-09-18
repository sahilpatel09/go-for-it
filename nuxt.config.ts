// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxt/image',
    '@nuxtjs/google-fonts'
  ],
  
  // TailwindCSS configuration
  tailwindcss: {
    configPath: '~/tailwind.config.js'
  },
  
  // Google Fonts configuration
  googleFonts: {
    families: {
      Inter: [400, 500, 600, 700, 800],
      Poppins: [400, 500, 600, 700, 800]
    },
    display: 'swap'
  },

  // App configuration
  app: {
    head: {
      title: 'Go For It Gas - Fast Fuel & Friendly Service',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'Your local gas station and convenience store. Fast fuel, snacks, and friendly service. Open daily with competitive prices.' },
        { name: 'keywords', content: 'gas station, fuel prices, convenience store, snacks, coffee, car wash, ATM' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
      ]
    }
  },

  // CSS configuration
  css: ['~/assets/css/main.css'],

  // Runtime config for environment variables
  runtimeConfig: {
    public: {
      siteUrl: 'https://goforitgas.com',
      siteName: 'Go For It Gas'
    }
  },

  // Image optimization
  image: {
    quality: 80,
    format: ['webp', 'avif'],
    screens: {
      xs: 320,
      sm: 640,
      md: 768,
      lg: 1024,
      xl: 1280,
      xxl: 1536,
    }
  },

  // SEO and performance
  nitro: {
    prerender: {
      routes: ['/']
    }
  }
})