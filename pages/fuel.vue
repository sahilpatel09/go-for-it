<template>
  <div>
    <!-- Hero Section -->
    <section class="relative h-64 flex items-center justify-center overflow-hidden">
      <div class="absolute inset-0">
        <NuxtImg 
          src="/images/fuel-pumps-hero.jpg" 
          alt="Fuel pumps at Go For It Gas"
          class="w-full h-full object-cover"
        />
        <div class="hero-overlay"></div>
      </div>
      <div class="relative z-10 text-center text-white">
        <h1 class="heading-2 mb-4 text-shadow-lg">Today's Fuel Prices</h1>
        <p class="text-lg text-shadow">Competitive prices updated daily</p>
      </div>
    </section>

    <!-- Fuel Prices Section -->
    <section class="py-16">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="heading-2 mb-4">Current Fuel Prices</h2>
          <p class="text-neutral-600 mb-6">Prices updated daily. Subject to change at station.</p>
          <div class="text-sm text-neutral-500">
            Last Updated: {{ new Date().toLocaleString() }}
          </div>
        </div>

        <!-- Price Cards -->
        <div class="grid md:grid-cols-2 gap-6 mb-12">
          <div class="card">
            <div class="card-body text-center">
              <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
                </svg>
              </div>
              <h3 class="heading-3 mb-2">Regular</h3>
              <div class="text-4xl font-bold text-primary-500 mb-2">$3.45</div>
              <p class="text-neutral-600">per gallon</p>
            </div>
          </div>

          <div class="card">
            <div class="card-body text-center">
              <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
                </svg>
              </div>
              <h3 class="heading-3 mb-2">Plus</h3>
              <div class="text-4xl font-bold text-primary-500 mb-2">$3.65</div>
              <p class="text-neutral-600">per gallon</p>
            </div>
          </div>

          <div class="card">
            <div class="card-body text-center">
              <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
                </svg>
              </div>
              <h3 class="heading-3 mb-2">Premium</h3>
              <div class="text-4xl font-bold text-primary-500 mb-2">$3.85</div>
              <p class="text-neutral-600">per gallon</p>
            </div>
          </div>

          <div class="card">
            <div class="card-body text-center">
              <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
                </svg>
              </div>
              <h3 class="heading-3 mb-2">Diesel</h3>
              <div class="text-4xl font-bold text-primary-500 mb-2">$3.95</div>
              <p class="text-neutral-600">per gallon</p>
            </div>
          </div>
        </div>

        <!-- Important Notice -->
        <div class="bg-accent-50 border border-accent-200 rounded-lg p-6 mb-8">
          <div class="flex items-start">
            <svg class="w-6 h-6 text-accent-600 mr-3 mt-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <div>
              <h4 class="font-semibold text-neutral-900 mb-2">Important Notice</h4>
              <p class="text-neutral-700">
                Fuel prices are updated daily and may change throughout the day. 
                Prices shown are for cash payments. Credit card payments may include additional fees. 
                Please check current prices at the pump before fueling.
              </p>
            </div>
          </div>
        </div>

        <!-- CTA Buttons -->
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <a href="https://www.google.com/maps?cid=12853947706317488130" target="_blank" class="btn-primary">
            Get Directions
          </a>
          <a href="tel:+16513952174" class="btn-secondary">
            Call Now
          </a>
        </div>
      </div>
    </section>

    <!-- Fuel Quality Information -->
    <section class="py-16 bg-neutral-50">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="heading-2 text-center mb-12">Quality Fuel Guarantee</h2>
        <div class="grid md:grid-cols-3 gap-8">
          <div class="text-center">
            <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
            </div>
            <h3 class="heading-4 mb-2">Top Quality</h3>
            <p class="text-neutral-600">We only sell premium quality fuel from trusted suppliers.</p>
          </div>
          
          <div class="text-center">
            <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
            </div>
            <h3 class="heading-4 mb-2">Fresh Daily</h3>
            <p class="text-neutral-600">Our tanks are refilled regularly to ensure fresh fuel.</p>
          </div>
          
          <div class="text-center">
            <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
              </svg>
            </div>
            <h3 class="heading-4 mb-2">24/7 Access</h3>
            <p class="text-neutral-600">Gas pumps are available 24 hours a day, 7 days a week.</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
useHead({
  title: 'Fuel Prices - Go For It Gas',
  meta: [
    { name: 'description', content: 'Current fuel prices at Go For It Gas. Competitive prices on regular, plus, premium, and diesel fuel. Updated daily.' },
    { name: 'keywords', content: 'fuel prices, gas prices, regular gas, premium gas, diesel, East Bethel' }
  ]
})
</script>
