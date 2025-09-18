<template>
  <div class="min-h-screen bg-white">
    <!-- Header -->
    <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-sm border-b border-neutral-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center py-4">
          <!-- Logo -->
          <div class="flex items-center">
            <NuxtLink to="/" class="flex items-center space-x-2">
              <div class="w-10 h-10 bg-primary-500 rounded-lg flex items-center justify-center">
                <span class="text-white font-bold text-xl">G</span>
              </div>
              <div>
                <h1 class="text-xl font-bold text-neutral-900">Go For It Gas</h1>
                <p class="text-xs text-neutral-600">Fast Fuel & Friendly Service</p>
              </div>
            </NuxtLink>
          </div>

          <!-- Desktop Navigation -->
          <nav class="hidden lg:flex items-center space-x-8">
            <NuxtLink to="/" class="nav-link" :class="{ 'nav-link-active': $route.path === '/' }">
              Home
            </NuxtLink>
            <NuxtLink to="/fuel" class="nav-link" :class="{ 'nav-link-active': $route.path === '/fuel' }">
              Fuel Prices
            </NuxtLink>
            <NuxtLink to="/store" class="nav-link" :class="{ 'nav-link-active': $route.path === '/store' }">
              Store
            </NuxtLink>
            <NuxtLink to="/services" class="nav-link" :class="{ 'nav-link-active': $route.path === '/services' }">
              Services
            </NuxtLink>
            <NuxtLink to="/promotions" class="nav-link" :class="{ 'nav-link-active': $route.path === '/promotions' }">
              Promotions
            </NuxtLink>
            <NuxtLink to="/contact" class="nav-link" :class="{ 'nav-link-active': $route.path === '/contact' }">
              Contact
            </NuxtLink>
          </nav>

          <!-- Desktop CTA Buttons -->
          <div class="hidden lg:flex items-center space-x-3">
            <a href="tel:+16513952174" class="btn-primary">
              Call Now
            </a>
            <a href="https://www.google.com/maps?cid=12853947706317488130" target="_blank" class="btn-outline">
              Get Directions
            </a>
          </div>

          <!-- Mobile Menu Button -->
          <button @click="mobileMenuOpen = !mobileMenuOpen" class="lg:hidden p-2">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path v-if="!mobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
              <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>

        <!-- Mobile Navigation -->
        <div v-if="mobileMenuOpen" class="lg:hidden py-4 border-t border-neutral-200">
          <nav class="flex flex-col space-y-4">
            <NuxtLink to="/" class="nav-link" @click="mobileMenuOpen = false">Home</NuxtLink>
            <NuxtLink to="/fuel" class="nav-link" @click="mobileMenuOpen = false">Fuel Prices</NuxtLink>
            <NuxtLink to="/store" class="nav-link" @click="mobileMenuOpen = false">Store</NuxtLink>
            <NuxtLink to="/services" class="nav-link" @click="mobileMenuOpen = false">Services</NuxtLink>
            <NuxtLink to="/promotions" class="nav-link" @click="mobileMenuOpen = false">Promotions</NuxtLink>
            <NuxtLink to="/contact" class="nav-link" @click="mobileMenuOpen = false">Contact</NuxtLink>
            <div class="pt-4 space-y-2">
              <a href="tel:+16513952174" class="btn-primary w-full text-center block">Call Now</a>
              <a href="https://www.google.com/maps?cid=12853947706317488130" target="_blank" class="btn-outline w-full text-center block">Get Directions</a>
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
    <footer class="bg-neutral-900 text-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div class="grid md:grid-cols-4 gap-8">
          <!-- Business Info -->
          <div class="md:col-span-2">
            <div class="flex items-center space-x-2 mb-4">
              <div class="w-8 h-8 bg-primary-500 rounded-lg flex items-center justify-center">
                <span class="text-white font-bold">G</span>
              </div>
              <h3 class="text-xl font-bold">Go For It Gas</h3>
            </div>
            <p class="text-neutral-300 mb-4">Your trusted local gas station and convenience store. Fast fuel, snacks, and friendly service.</p>
            
            <div class="space-y-2">
              <div class="flex items-center">
                <svg class="w-5 h-5 text-primary-500 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                </svg>
                <span>3255 Viking Blvd NE, East Bethel, MN 55092</span>
              </div>
              <div class="flex items-center">
                <svg class="w-5 h-5 text-primary-500 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
                </svg>
                <a href="tel:+16513952174" class="hover:text-primary-500 transition-colors">(651) 395-2174</a>
              </div>
              <div class="flex items-center">
                <svg class="w-5 h-5 text-primary-500 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                </svg>
                <a href="mailto:info@goforitgas.com" class="hover:text-primary-500 transition-colors">info@goforitgas.com</a>
              </div>
            </div>
          </div>

          <!-- Hours -->
          <div>
            <h4 class="text-lg font-semibold mb-4">Store Hours</h4>
            <div class="space-y-2 text-sm">
              <div class="flex justify-between">
                <span>Monday</span>
                <span>6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span>Tuesday</span>
                <span>6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span>Wednesday</span>
                <span>6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span>Thursday</span>
                <span>6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span>Friday</span>
                <span>6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span>Saturday</span>
                <span>6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span>Sunday</span>
                <span>6:00 AM - 10:00 PM</span>
              </div>
              <p class="text-xs text-neutral-400 mt-2">*Gas pumps available 24/7</p>
            </div>
          </div>

          <!-- Quick Links -->
          <div>
            <h4 class="text-lg font-semibold mb-4">Quick Links</h4>
            <div class="space-y-2 text-sm">
              <NuxtLink to="/fuel" class="block hover:text-primary-500 transition-colors">Fuel Prices</NuxtLink>
              <NuxtLink to="/store" class="block hover:text-primary-500 transition-colors">Store Products</NuxtLink>
              <NuxtLink to="/services" class="block hover:text-primary-500 transition-colors">Services</NuxtLink>
              <NuxtLink to="/promotions" class="block hover:text-primary-500 transition-colors">Promotions</NuxtLink>
              <NuxtLink to="/about" class="block hover:text-primary-500 transition-colors">About Us</NuxtLink>
              <NuxtLink to="/contact" class="block hover:text-primary-500 transition-colors">Contact</NuxtLink>
            </div>
          </div>
        </div>

        <!-- Bottom Bar -->
        <div class="border-t border-neutral-800 mt-8 pt-8 flex flex-col md:flex-row justify-between items-center">
          <p class="text-sm text-neutral-400">&copy; 2024 Go For It Gas. All rights reserved.</p>
          <div class="flex space-x-6 mt-4 md:mt-0">
            <NuxtLink to="/privacy" class="text-sm text-neutral-400 hover:text-primary-500 transition-colors">Privacy Policy</NuxtLink>
            <NuxtLink to="/terms" class="text-sm text-neutral-400 hover:text-primary-500 transition-colors">Terms of Service</NuxtLink>
          </div>
        </div>
      </div>
    </footer>

    <!-- Floating CTA Bar (Mobile Only) -->
    <div class="floating-cta">
      <div class="flex justify-around py-3">
        <a href="tel:+16513952174" class="flex flex-col items-center space-y-1 text-xs">
          <svg class="w-6 h-6 text-primary-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
          </svg>
          <span class="text-neutral-700 font-medium">Call</span>
        </a>
        <a href="https://www.google.com/maps?cid=12853947706317488130" target="_blank" class="flex flex-col items-center space-y-1 text-xs">
          <svg class="w-6 h-6 text-primary-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
          </svg>
          <span class="text-neutral-700 font-medium">Directions</span>
        </a>
        <button @click="showHours = !showHours" class="flex flex-col items-center space-y-1 text-xs">
          <svg class="w-6 h-6 text-primary-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
          </svg>
          <span class="text-neutral-700 font-medium">Hours</span>
        </button>
      </div>
      
      <!-- Hours Modal -->
      <div v-if="showHours" class="absolute bottom-full left-0 right-0 bg-white border-t border-neutral-200 p-4 shadow-strong">
        <h4 class="font-semibold mb-2">Store Hours</h4>
        <div class="space-y-1 text-sm">
              <div class="flex justify-between">
                <span>Monday</span>
                <span>6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span>Tuesday</span>
                <span>6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span>Wednesday</span>
                <span>6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span>Thursday</span>
                <span>6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span>Friday</span>
                <span>6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span>Saturday</span>
                <span>6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span>Sunday</span>
                <span>6:00 AM - 10:00 PM</span>
              </div>
          <p class="text-xs text-neutral-500 mt-2">*Gas pumps available 24/7</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const mobileMenuOpen = ref(false)
const showHours = ref(false)

// Close mobile menu when route changes
watch(() => useRoute().path, () => {
  mobileMenuOpen.value = false
})
</script>
