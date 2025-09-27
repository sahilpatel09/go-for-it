<template>
  <div>
    <!-- Hero Section -->
    <section class="relative min-h-screen flex items-center justify-center overflow-hidden" style="background: linear-gradient(135deg, #0A0A0A 0%, #1A1A1A 50%, #0F0F0F 100%);">
      <div class="absolute inset-0">
        <NuxtImg 
          :src="brandData.heroImage" 
          :alt="`${brandData.name} - Premium Spirits at Go For It Liquor East Bethel, MN`"
          class="w-full h-full object-cover opacity-25"
          loading="eager"
          preload
        />
        <div class="absolute inset-0" style="background: linear-gradient(135deg, rgba(10, 10, 10, 0.4) 0%, rgba(26, 26, 26, 0.3) 50%, rgba(15, 15, 15, 0.4) 100%);"></div>
      </div>
      
      <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <div class="mb-8">
          <div class="w-24 h-1 mx-auto mb-6" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
        </div>
        <h1 class="text-6xl md:text-8xl font-bold mb-8 leading-tight" style="color: #F5F5F5; font-family: 'Playfair Display', serif; letter-spacing: -0.02em;">
          {{ brandData.name }}<br><span style="color: #D4AF37;">Premium Collection</span>
        </h1>
        <div class="w-32 h-1 mx-auto mb-8" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
        <p class="text-xl md:text-2xl mb-12 max-w-3xl mx-auto leading-relaxed" style="color: #E5E5E5; font-family: 'Inter', sans-serif; font-weight: 300;">
          {{ brandData.description }}<br>
          <span style="color: #D4AF37;">Available at Go For It Liquor in East Bethel, MN</span>
        </p>
        <div class="flex flex-col sm:flex-row gap-6 justify-center">
          <a href="https://maps.app.goo.gl/H1gsh7KUfgrg6ek49" target="_blank" class="group px-10 py-4 text-lg font-semibold rounded-lg transition-all duration-500 border-2" style="border-color: #D4AF37; color: #D4AF37; background: transparent; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#D4AF37'; this.style.color='#0A0A0A'; this.style.boxShadow='0 0 30px rgba(212, 175, 55, 0.4)';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#D4AF37'; this.style.boxShadow='none';">
            <span class="flex items-center justify-center">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
              </svg>
              Visit Our Store
            </span>
          </a>
          <a href="tel:+16513952174" class="group px-10 py-4 text-lg font-semibold rounded-lg transition-all duration-500 border-2" style="border-color: #D4AF37; color: #D4AF37; background: transparent; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#D4AF37'; this.style.color='#0A0A0A'; this.style.boxShadow='0 0 30px rgba(212, 175, 55, 0.4)';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#D4AF37'; this.style.boxShadow='none';">
            <span class="flex items-center justify-center">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
              </svg>
              Call Now
            </span>
          </a>
        </div>
      </div>
    </section>

    <!-- Product Collection -->
    <section class="py-24" style="background: linear-gradient(135deg, #0A0A0A 0%, #1A1A1A 50%, #0F0F0F 100%);">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-20">
          <div class="w-24 h-1 mx-auto mb-6" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
          <h2 class="text-5xl md:text-6xl font-bold mb-8" style="color: #F5F5F5; font-family: 'Playfair Display', serif; letter-spacing: -0.02em;">{{ brandData.name }} Collection</h2>
          <p class="text-xl max-w-4xl mx-auto leading-relaxed" style="color: #E5E5E5; font-family: 'Inter', sans-serif; font-weight: 300;">
            Discover our curated selection of {{ brandData.name }} products available at Go For It Liquor
          </p>
        </div>
        
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div 
            v-for="product in brandData.products" 
            :key="product.name"
            class="group relative overflow-hidden rounded-2xl transition-all duration-700 hover:scale-105" 
            style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 1px solid rgba(212, 175, 55, 0.1);"
          >
            <div class="p-8 text-center">
              <div class="mb-6">
                <NuxtImg 
                  :src="product.image" 
                  :alt="`${product.name} - ${brandData.name} Premium Spirits`"
                  class="w-48 h-48 object-cover mx-auto rounded-lg drop-shadow-2xl transition-transform duration-500 group-hover:scale-110"
                  loading="lazy"
                />
              </div>
              <div class="mb-4">
                <div class="w-16 h-0.5 mx-auto mb-3" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
                <h3 class="text-2xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">{{ product.name }}</h3>
                <p class="text-sm mb-2" style="color: #D4AF37; font-family: 'Inter', sans-serif; font-weight: 500;">{{ product.category }}</p>
                <p v-if="product.priceRange" class="text-sm" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">{{ product.priceRange }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Brand Story -->
    <section class="py-24" style="background: linear-gradient(135deg, #0A0A0A 0%, #1A1A1A 50%, #0F0F0F 100%);">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid lg:grid-cols-2 gap-12 items-center">
          <div>
            <div class="w-16 h-0.5 mb-6" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
            <h2 class="text-4xl font-bold mb-6" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">About {{ brandData.name }}</h2>
            <p class="text-lg mb-6 leading-relaxed" style="color: #E5E5E5; font-family: 'Inter', sans-serif; font-weight: 300;">
              {{ brandData.story }}
            </p>
            <div class="space-y-4">
              <div class="flex items-center">
                <svg class="w-6 h-6 mr-4" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                </svg>
                <span style="color: #E5E5E5; font-family: 'Inter', sans-serif;">Available at Go For It Liquor</span>
              </div>
              <div class="flex items-center">
                <svg class="w-6 h-6 mr-4" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                </svg>
                <span style="color: #E5E5E5; font-family: 'Inter', sans-serif;">Located in East Bethel, MN</span>
              </div>
              <div class="flex items-center">
                <svg class="w-6 h-6 mr-4" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"></path>
                </svg>
                <span style="color: #E5E5E5; font-family: 'Inter', sans-serif;">Competitive pricing</span>
              </div>
            </div>
          </div>
          <div class="relative">
            <NuxtImg 
              :src="brandData.storyImage" 
              :alt="`${brandData.name} brand story and heritage`"
              class="w-full h-96 object-cover rounded-2xl shadow-2xl"
              loading="lazy"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-black/50 to-transparent rounded-2xl"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- Call to Action -->
    <section class="py-24" style="background: linear-gradient(135deg, #0A0A0A 0%, #1A1A1A 50%, #0F0F0F 100%);">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <div class="mb-8">
          <div class="w-24 h-1 mx-auto mb-6" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
          <h2 class="text-4xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Ready to Experience {{ brandData.name }}?</h2>
          <p class="text-xl mb-8" style="color: #E5E5E5; font-family: 'Inter', sans-serif; font-weight: 300;">Visit Go For It Liquor in East Bethel, MN to explore our {{ brandData.name }} collection</p>
        </div>
        <div class="flex flex-col sm:flex-row gap-6 justify-center">
          <a href="https://maps.app.goo.gl/H1gsh7KUfgrg6ek49" target="_blank" class="group px-10 py-4 text-lg font-semibold rounded-lg transition-all duration-500 border-2" style="border-color: #D4AF37; color: #D4AF37; background: transparent; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#D4AF37'; this.style.color='#0A0A0A'; this.style.boxShadow='0 0 30px rgba(212, 175, 55, 0.4)';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#D4AF37'; this.style.boxShadow='none';">
            <span class="flex items-center justify-center">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
              </svg>
              Get Directions
            </span>
          </a>
          <a href="tel:+16513952174" class="group px-10 py-4 text-lg font-semibold rounded-lg transition-all duration-500 border-2" style="border-color: #D4AF37; color: #D4AF37; background: transparent; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#D4AF37'; this.style.color='#0A0A0A'; this.style.boxShadow='0 0 30px rgba(212, 175, 55, 0.4)';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#D4AF37'; this.style.boxShadow='none';">
            <span class="flex items-center justify-center">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
              </svg>
              Call Now
            </span>
          </a>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
// Get the brand parameter from the route
const route = useRoute()
const brand = route.params.brand

// Brand data - in a real app, this would come from an API or CMS
const brandData = {
  'jack-daniels': {
    name: 'Jack Daniel\'s',
    description: 'Tennessee\'s finest whiskey, crafted with tradition and excellence since 1866.',
    story: 'Jack Daniel\'s is America\'s oldest registered distillery, producing Tennessee whiskey with a unique charcoal mellowing process. Each bottle represents over 150 years of craftsmanship and tradition.',
    heroImage: '/images/brands/jack-daniels.jpg',
    storyImage: '/images/brands/jack-daniel.png',
    products: [
      {
        name: 'Jack Daniel\'s Old No. 7',
        category: 'Tennessee Whiskey',
        image: '/images/brands/jack-daniel.png',
        priceRange: '$25-35'
      },
      {
        name: 'Jack Daniel\'s Gentleman Jack',
        category: 'Tennessee Whiskey',
        image: '/images/brands/jack-daniels.jpg',
        priceRange: '$35-45'
      }
    ]
  },
  'crown-royal': {
    name: 'Crown Royal',
    description: 'Canadian whisky crafted with precision and care, delivering exceptional smoothness.',
    story: 'Crown Royal was created in 1939 to honor the royal visit of King George VI and Queen Elizabeth. It represents the pinnacle of Canadian whisky craftsmanship.',
    heroImage: '/images/brands/crown-royal-dark.png',
    storyImage: '/images/brands/crown-royal.jpeg',
    products: [
      {
        name: 'Crown Royal Deluxe',
        category: 'Canadian Whisky',
        image: '/images/brands/crown-royal-dark.png',
        priceRange: '$30-40'
      }
    ]
  }
}

// Get the current brand data or redirect to 404
const currentBrand = brandData[brand]
if (!currentBrand) {
  throw createError({
    statusCode: 404,
    statusMessage: 'Brand not found'
  })
}

// SEO Meta
useHead({
  title: `${currentBrand.name} — Premium Spirits at Go For It Liquor East Bethel, MN`,
  meta: [
    { name: 'description', content: `Discover ${currentBrand.name} premium spirits at Go For It Liquor in East Bethel, MN. ${currentBrand.description} Call (651) 395-2174 or visit us today.` },
    { name: 'keywords', content: `${currentBrand.name}, premium spirits, East Bethel MN, liquor store, ${currentBrand.name.toLowerCase()} collection, Go For It Liquor` },
    { name: 'canonical', content: `https://go-for-it-wheat.vercel.app/brands/${brand}` }
  ],
  link: [
    { rel: 'sitemap', href: '/sitemap.xml', type: 'application/xml' }
  ],
  script: [
    {
      type: 'application/ld+json',
      innerHTML: JSON.stringify({
        "@context": "https://schema.org",
        "@type": "Product",
        "name": currentBrand.name,
        "description": currentBrand.description,
        "image": `https://go-for-it-wheat.vercel.app${currentBrand.heroImage}`,
        "brand": {
          "@type": "Brand",
          "name": currentBrand.name
        },
        "offers": {
          "@type": "Offer",
          "availability": "https://schema.org/InStock",
          "priceRange": "$$",
          "seller": {
            "@type": "LiquorStore",
            "name": "Go For It Liquor",
            "address": {
              "@type": "PostalAddress",
              "streetAddress": "3255 Viking Blvd NE",
              "addressLocality": "East Bethel",
              "addressRegion": "MN",
              "postalCode": "55092",
              "addressCountry": "US"
            }
          }
        }
      })
    }
  ]
})
</script>
