<template>
  <div class="min-h-screen" style="background-color: #121212;">
    <!-- Header -->
    <header class="sticky top-0 z-40 backdrop-blur-sm" style="background-color: rgba(18, 18, 18, 0.95); border-bottom: 1px solid #1C1C1C;">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center py-4">
          <!-- Logo -->
          <div class="flex items-center">
            <NuxtLink to="/" class="flex items-center space-x-3">
              <div class="w-12 h-12 rounded-lg flex items-center justify-center shadow-lg" style="background: linear-gradient(135deg, #C9A227 0%, #B8941F 100%);">
                <span class="font-bold text-xl" style="color: #1C1C1C;">G</span>
              </div>
              <div>
                <h1 class="text-xl font-bold" style="color: #EAEAEA; font-family: 'Playfair Display', serif;">Go For It Liquor</h1>
                <p class="text-xs" style="color: #C9A227; font-family: 'Inter', sans-serif;">Your Local Liquor Destination</p>
              </div>
            </NuxtLink>
          </div>

          <!-- Desktop Navigation -->
          <nav class="hidden lg:flex items-center space-x-8">
            <NuxtLink to="/" class="transition-colors font-medium" style="color: #EAEAEA; font-family: 'Inter', sans-serif;" :style="{ color: $route.path === '/' ? '#C9A227' : '#EAEAEA' }" onmouseover="this.style.color='#C9A227';" onmouseout="this.style.color=$route.path === '/' ? '#C9A227' : '#EAEAEA';">
              Home
            </NuxtLink>
            <!-- <NuxtLink to="/store" class="transition-colors font-medium" style="color: #EAEAEA; font-family: 'Inter', sans-serif;" :style="{ color: $route.path === '/store' ? '#C9A227' : '#EAEAEA' }" onmouseover="this.style.color='#C9A227';" onmouseout="this.style.color=$route.path === '/store' ? '#C9A227' : '#EAEAEA';">
              Store
            </NuxtLink> -->
            <NuxtLink to="/liquor" class="transition-colors font-medium" style="color: #EAEAEA; font-family: 'Inter', sans-serif;" :style="{ color: $route.path === '/liquor' ? '#C9A227' : '#EAEAEA' }" onmouseover="this.style.color='#C9A227';" onmouseout="this.style.color=$route.path === '/liquor' ? '#C9A227' : '#EAEAEA';">
              Liquor
            </NuxtLink>

            <NuxtLink to="/contact" class="transition-colors font-medium" style="color: #EAEAEA; font-family: 'Inter', sans-serif;" :style="{ color: $route.path === '/contact' ? '#C9A227' : '#EAEAEA' }" onmouseover="this.style.color='#C9A227';" onmouseout="this.style.color=$route.path === '/contact' ? '#C9A227' : '#EAEAEA';">
              Contact
            </NuxtLink>
          </nav>

          <!-- Desktop CTA Buttons -->
          <div class="hidden lg:flex items-center space-x-3">
            <a href="tel:+16513952174" class="px-4 py-2 rounded-lg font-semibold transition-colors duration-300" style="background-color: #C9A227; color: #1C1C1C; font-family: 'Inter', sans-serif;">
              Call Now
            </a>
            <a href="https://maps.app.goo.gl/H1gsh7KUfgrg6ek49" target="_blank" class="px-4 py-2 rounded-lg font-semibold transition-all duration-300 border-2" style="border-color: #C9A227; color: #C9A227; background: transparent; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#C9A227'; this.style.color='#1C1C1C';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#C9A227';">
              Get Directions
            </a>
          </div>

          <!-- Mobile Menu Button -->
          <button @click="mobileMenuOpen = !mobileMenuOpen" class="lg:hidden p-2" style="color: #EAEAEA;">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path v-if="!mobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
              <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>

        <!-- Mobile Navigation -->
        <div v-if="mobileMenuOpen" class="lg:hidden py-4" style="border-top: 1px solid #1C1C1C;">
          <nav class="flex flex-col space-y-4">
            <NuxtLink to="/" class="transition-colors font-medium" style="color: #EAEAEA; font-family: 'Inter', sans-serif;" @click="mobileMenuOpen = false" onmouseover="this.style.color='#C9A227';" onmouseout="this.style.color='#EAEAEA';">Home</NuxtLink>
            <NuxtLink to="/liquor" class="transition-colors font-medium" style="color: #EAEAEA; font-family: 'Inter', sans-serif;" @click="mobileMenuOpen = false" onmouseover="this.style.color='#C9A227';" onmouseout="this.style.color='#EAEAEA';">Liquor</NuxtLink>
            <NuxtLink to="/contact" class="transition-colors font-medium" style="color: #EAEAEA; font-family: 'Inter', sans-serif;" @click="mobileMenuOpen = false" onmouseover="this.style.color='#C9A227';" onmouseout="this.style.color='#EAEAEA';">Contact</NuxtLink>
            <div class="pt-4 space-y-2">
              <a href="tel:+16513952174" class="w-full text-center block py-2 rounded-lg font-semibold transition-colors duration-300" style="background-color: #C9A227; color: #1C1C1C; font-family: 'Inter', sans-serif;">Call Now</a>
              <a href="https://maps.app.goo.gl/H1gsh7KUfgrg6ek49" target="_blank" class="w-full text-center block py-2 rounded-lg font-semibold transition-all duration-300 border-2" style="border-color: #C9A227; color: #C9A227; background: transparent; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#C9A227'; this.style.color='#1C1C1C';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#C9A227';">Get Directions</a>
            </div>
          </nav>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main>
      <slot />
    </main>

    <!-- Footer -->
    <footer style="background-color: #121212;">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div class="grid md:grid-cols-4 gap-8">
          <!-- Business Info -->
          <div class="md:col-span-2">
            <div class="flex items-center space-x-3 mb-4">
              <div class="w-10 h-10 rounded-lg flex items-center justify-center shadow-lg" style="background: linear-gradient(135deg, #C9A227 0%, #B8941F 100%);">
                <span class="font-bold" style="color: #1C1C1C;">G</span>
              </div>
              <h3 class="text-xl font-bold" style="color: #EAEAEA; font-family: 'Playfair Display', serif;">Go For It Liquor</h3>
            </div>
            <p class="mb-4" style="color: #EAEAEA; font-family: 'Inter', sans-serif;">Go For It Liquor — Premium Spirits, Exceptional Taste</p>
            <p class="text-sm mb-6" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">Your destination for curated spirits, rare vintages, and expert guidance in East Bethel, MN.</p>
            
            <div class="space-y-2">
              <div class="flex items-center">
                <svg class="w-5 h-5 mr-3" style="color: #C9A227;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                </svg>
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">3255 Viking Blvd NE, East Bethel, MN 55092</span>
              </div>
              <div class="flex items-center">
                <svg class="w-5 h-5 mr-3" style="color: #C9A227;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
                </svg>
                <a href="tel:+16513952174" class="transition-colors" style="color: #EAEAEA; font-family: 'Inter', sans-serif;" onmouseover="this.style.color='#C9A227';" onmouseout="this.style.color='#EAEAEA';">(651) 395-2174</a>
              </div>
              <div class="flex items-center">
                <svg class="w-5 h-5 mr-3" style="color: #C9A227;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                </svg>
                <a href="mailto:info@goforitgas.com" class="transition-colors" style="color: #EAEAEA; font-family: 'Inter', sans-serif;" onmouseover="this.style.color='#C9A227';" onmouseout="this.style.color='#EAEAEA';">info@goforitgas.com</a>
              </div>
            </div>
          </div>

          <!-- Hours -->
          <div>
            <h4 class="text-lg font-semibold mb-4" style="color: #EAEAEA; font-family: 'Inter', sans-serif;">Store Hours</h4>
            <div class="space-y-2 text-sm">
              <div class="flex justify-between">
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">Monday</span>
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">Tuesday</span>
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">Wednesday</span>
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">Thursday</span>
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">Friday</span>
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">Saturday</span>
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">Sunday</span>
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">6:00 AM - 10:00 PM</span>
              </div>
              <p class="text-xs mt-2" style="color: #EAEAEA; font-family: 'Inter', sans-serif;">*Gas pumps available 24/7</p>
            </div>
          </div>

          <!-- Quick Links -->
          <div>
            <h4 class="text-lg font-semibold mb-4" style="color: #EAEAEA; font-family: 'Inter', sans-serif;">Quick Links</h4>
            <div class="space-y-2 text-sm">
              <NuxtLink to="/" class="block transition-colors" style="color: #EAEAEA; font-family: 'Inter', sans-serif;" onmouseover="this.style.color='#C9A227';" onmouseout="this.style.color='#EAEAEA';">Home</NuxtLink>
              <NuxtLink to="/liquor" class="block transition-colors" style="color: #EAEAEA; font-family: 'Inter', sans-serif;" onmouseover="this.style.color='#C9A227';" onmouseout="this.style.color='#EAEAEA';">Liquor</NuxtLink>
              <NuxtLink to="/contact" class="block transition-colors" style="color: #EAEAEA; font-family: 'Inter', sans-serif;" onmouseover="this.style.color='#C9A227';" onmouseout="this.style.color='#EAEAEA';">Contact</NuxtLink>
            </div>
          </div>
        </div>

        <!-- Bottom Bar -->
        <div class="mt-8 pt-8 flex flex-col md:flex-row justify-between items-center" style="border-top: 1px solid #1C1C1C;">
          <p class="text-sm" style="color: #EAEAEA; font-family: 'Inter', sans-serif;">&copy; {{ currentYear }} Go For It Liquor. All rights reserved.</p>
          <div class="flex space-x-6 mt-4 md:mt-0">
            <NuxtLink to="/privacy" class="text-sm transition-colors" style="color: #EAEAEA; font-family: 'Inter', sans-serif;" onmouseover="this.style.color='#C9A227';" onmouseout="this.style.color='#EAEAEA';">Privacy Policy</NuxtLink>
            <NuxtLink to="/terms" class="text-sm transition-colors" style="color: #EAEAEA; font-family: 'Inter', sans-serif;" onmouseover="this.style.color='#C9A227';" onmouseout="this.style.color='#EAEAEA';">Terms of Service</NuxtLink>
          </div>
        </div>
      </div>
    </footer>

    <!-- Floating CTA Bar (Mobile Only) -->
    <div class="fixed bottom-0 left-0 right-0 lg:hidden z-50" style="background-color: #121212; border-top: 1px solid #1C1C1C;">
      <div class="flex justify-around py-3">
        <a href="tel:+16513952174" class="flex flex-col items-center space-y-1 text-xs">
          <svg class="w-6 h-6" style="color: #C9A227;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
          </svg>
          <span class="font-medium" style="color: #EAEAEA; font-family: 'Inter', sans-serif;">Call</span>
        </a>
        <a href="https://maps.app.goo.gl/H1gsh7KUfgrg6ek49" target="_blank" class="flex flex-col items-center space-y-1 text-xs">
          <svg class="w-6 h-6" style="color: #C9A227;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
          </svg>
          <span class="font-medium" style="color: #EAEAEA; font-family: 'Inter', sans-serif;">Directions</span>
        </a>
        <button @click="showHours = !showHours" class="flex flex-col items-center space-y-1 text-xs">
          <svg class="w-6 h-6" style="color: #C9A227;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
          </svg>
          <span class="font-medium" style="color: #EAEAEA; font-family: 'Inter', sans-serif;">Hours</span>
        </button>
      </div>
      
      <!-- Hours Modal -->
      <div v-if="showHours" class="absolute bottom-full left-0 right-0 p-4 shadow-2xl" style="background-color: #121212; border-top: 1px solid #1C1C1C;">
        <h4 class="font-semibold mb-2" style="color: #EAEAEA; font-family: 'Inter', sans-serif;">Store Hours</h4>
        <div class="space-y-1 text-sm">
              <div class="flex justify-between">
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">Monday</span>
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">Tuesday</span>
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">Wednesday</span>
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">Thursday</span>
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">Friday</span>
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">Saturday</span>
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">Sunday</span>
                <span style="color: #EAEAEA; font-family: 'Inter', sans-serif;">6:00 AM - 10:00 PM</span>
              </div>
          <p class="text-xs mt-2" style="color: #EAEAEA; font-family: 'Inter', sans-serif;">*Gas pumps available 24/7</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const mobileMenuOpen = ref(false)
const showHours = ref(false)

// Dynamic year for copyright
const currentYear = new Date().getFullYear()

// Close mobile menu when route changes
watch(() => useRoute().path, () => {
  mobileMenuOpen.value = false
})

// Add Google Fonts
useHead({
  link: [
    {
      rel: 'preconnect',
      href: 'https://fonts.googleapis.com'
    },
    {
      rel: 'preconnect',
      href: 'https://fonts.gstatic.com',
      crossorigin: ''
    },
    {
      rel: 'stylesheet',
      href: 'https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Inter:wght@300;400;500;600;700&display=swap'
    }
  ]
})
</script>
