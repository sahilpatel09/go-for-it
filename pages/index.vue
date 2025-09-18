<template>
  <div>
    <!-- Page Header -->
    <section class="relative py-16 bg-gradient-to-r from-primary-600 to-primary-700">
      <div class="absolute inset-0">
        <NuxtImg 
          src="/img.webp" 
          alt="Go For It Gas Station - 3255 Viking Blvd NE, East Bethel, MN"
          class="w-full h-full object-cover opacity-40"
          loading="eager"
          preload
        />
      </div>
      
      <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="heading-1 text-white mb-4">
          Fast Fuel & Friendly Service
        </h1>
        <p class="text-xl text-white/90 mb-8">
          Your local stop for gas, snacks, and more in East Bethel, MN.
        </p>
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

    <!-- Fuel Prices Ticker -->
    <section class="bg-primary-500 py-4">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col md:flex-row items-center justify-between text-white">
          <h2 class="text-lg font-semibold mb-4 md:mb-0">Today's Fuel Prices</h2>
          <div class="flex flex-wrap gap-6 text-center">
            <div class="price-ticker">
              <div class="text-sm">Regular</div>
              <div class="text-xl font-bold">$3.45</div>
            </div>
            <div class="price-ticker">
              <div class="text-sm">Plus</div>
              <div class="text-xl font-bold">$3.65</div>
            </div>
            <div class="price-ticker">
              <div class="text-sm">Premium</div>
              <div class="text-xl font-bold">$3.85</div>
            </div>
            <div class="price-ticker">
              <div class="text-sm">Diesel</div>
              <div class="text-xl font-bold">$3.95</div>
            </div>
          </div>
          <div class="text-sm text-primary-100 mt-4 md:mt-0">
            Last Updated: {{ new Date().toLocaleString() }}
          </div>
        </div>
      </div>
    </section>

    <!-- Promotions Strip -->
    <section class="py-12 bg-neutral-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="heading-2 text-center mb-8">Current Promotions</h2>
        <div class="grid md:grid-cols-3 gap-6">
          <div class="card relative overflow-hidden">
            <div class="promo-badge">Save $0.10</div>
            <NuxtImg 
              src="/images/coffee-promo.jpg" 
              alt="Fresh Coffee Promotion"
              class="w-full h-48 object-cover"
            />
            <div class="card-body">
              <h3 class="heading-4 mb-2">Fresh Coffee</h3>
              <p class="text-neutral-600 mb-4">Get $0.10 off any large coffee. Available all day!</p>
              <button class="btn-primary w-full">Visit Store</button>
            </div>
          </div>
          
          <div class="card relative overflow-hidden">
            <div class="promo-badge">Buy 2 Get 1</div>
            <NuxtImg 
              src="/images/snacks-promo.jpg" 
              alt="Snacks Promotion"
              class="w-full h-48 object-cover"
            />
            <div class="card-body">
              <h3 class="heading-4 mb-2">Snack Attack</h3>
              <p class="text-neutral-600 mb-4">Buy 2 snacks, get 1 free. Mix and match any snacks!</p>
              <button class="btn-primary w-full">Visit Store</button>
            </div>
          </div>
          
          <div class="card relative overflow-hidden">
            <div class="promo-badge">$2 Off</div>
            <NuxtImg 
              src="/images/car-wash-promo.jpg" 
              alt="Car Wash Promotion"
              class="w-full h-48 object-cover"
            />
            <div class="card-body">
              <h3 class="heading-4 mb-2">Car Wash Special</h3>
              <p class="text-neutral-600 mb-4">$2 off premium car wash. Valid through this month.</p>
              <button class="btn-primary w-full">Get Service</button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Convenience Store Highlights -->
    <section class="py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="heading-2 text-center mb-12">Convenience Store</h2>
        <div class="grid md:grid-cols-4 gap-6">
          <div class="card text-center">
            <div class="card-body">
              <div class="w-16 h-16 bg-accent-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-8 h-8 text-accent-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path>
                </svg>
              </div>
              <h3 class="heading-4 mb-2">Fresh Coffee</h3>
              <p class="text-neutral-600">Premium coffee blends, hot and iced options available.</p>
            </div>
          </div>
          
          <div class="card text-center">
            <div class="card-body">
              <div class="w-16 h-16 bg-accent-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-8 h-8 text-accent-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
              </div>
              <h3 class="heading-4 mb-2">Hot Food</h3>
              <p class="text-neutral-600">Fresh sandwiches, hot dogs, and daily specials.</p>
            </div>
          </div>
          
          <div class="card text-center">
            <div class="card-body">
              <div class="w-16 h-16 bg-accent-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-8 h-8 text-accent-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path>
                </svg>
              </div>
              <h3 class="heading-4 mb-2">Snacks & Drinks</h3>
              <p class="text-neutral-600">Wide variety of chips, candy, and cold beverages.</p>
            </div>
          </div>
          
          <div class="card text-center">
            <div class="card-body">
              <div class="w-16 h-16 bg-accent-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-8 h-8 text-accent-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
              </div>
              <h3 class="heading-4 mb-2">Essentials</h3>
              <p class="text-neutral-600">Everyday items, tobacco products, and lottery tickets.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Services Section -->
    <section class="py-16 bg-neutral-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="heading-2 text-center mb-12">Additional Services</h2>
        <div class="grid md:grid-cols-4 gap-6">
          <div class="text-center">
            <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"></path>
              </svg>
            </div>
            <h3 class="heading-4 mb-2">ATM</h3>
            <p class="text-neutral-600">24/7 ATM access for your convenience.</p>
          </div>
          
          <div class="text-center">
            <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
              </svg>
            </div>
            <h3 class="heading-4 mb-2">Car Wash</h3>
            <p class="text-neutral-600">Professional car wash services available.</p>
          </div>
          
          <div class="text-center">
            <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 10-9.78 2.096A4.001 4.001 0 003 15z"></path>
              </svg>
            </div>
            <h3 class="heading-4 mb-2">Air & Water</h3>
            <p class="text-neutral-600">Free air and water for your vehicle.</p>
          </div>
          
          <div class="text-center">
            <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
              </svg>
            </div>
            <h3 class="heading-4 mb-2">EV Charging</h3>
            <p class="text-neutral-600">Electric vehicle charging stations available.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Map & Hours Section -->
    <section class="py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid lg:grid-cols-2 gap-12">
          <!-- Map -->
          <div class="card">
            <div class="card-body">
              <h3 class="heading-3 mb-4">Find Us</h3>
              <div class="bg-neutral-200 h-64 rounded-lg flex items-center justify-center mb-4">
                <p class="text-neutral-500">Interactive Google Map would be embedded here</p>
              </div>
              <a href="https://www.google.com/maps?cid=12853947706317488130" target="_blank" class="btn-primary w-full">
                Get Directions
              </a>
            </div>
          </div>
          
          <!-- Hours -->
          <div class="card">
            <div class="card-body">
              <h3 class="heading-3 mb-4">Store Hours</h3>
              <div class="space-y-3 mb-6">
                <div class="flex justify-between items-center">
                  <span class="font-medium">Monday</span>
                  <span class="text-neutral-600">6:00 AM - 10:00 PM</span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="font-medium">Tuesday</span>
                  <span class="text-neutral-600">6:00 AM - 10:00 PM</span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="font-medium">Wednesday</span>
                  <span class="text-neutral-600">6:00 AM - 10:00 PM</span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="font-medium">Thursday</span>
                  <span class="text-neutral-600">6:00 AM - 10:00 PM</span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="font-medium">Friday</span>
                  <span class="text-neutral-600">6:00 AM - 10:00 PM</span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="font-medium">Saturday</span>
                  <span class="text-neutral-600">6:00 AM - 10:00 PM</span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="font-medium">Sunday</span>
                  <span class="text-neutral-600">6:00 AM - 10:00 PM</span>
                </div>
              </div>
              <div class="bg-accent-50 border border-accent-200 rounded-lg p-4 mb-6">
                <div class="flex items-center">
                  <div class="w-3 h-3 bg-green-500 rounded-full mr-3"></div>
                  <span class="font-semibold text-green-700">Open Now</span>
                </div>
                <p class="text-sm text-neutral-600 mt-1">Closes at 10:00 PM today</p>
              </div>
              <p class="text-sm text-neutral-500">*Gas pumps available 24/7</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
// SEO Meta
useHead({
  title: 'Go For It Gas - Fast Fuel & Friendly Service',
  meta: [
    { name: 'description', content: 'Your local gas station and convenience store. Fast fuel, snacks, and friendly service. Open daily with competitive prices and 24/7 gas pumps.' },
    { name: 'keywords', content: 'gas station, fuel prices, convenience store, snacks, coffee, car wash, ATM, East Bethel' }
  ]
})
</script>
