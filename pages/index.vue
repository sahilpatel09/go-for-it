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
    <!-- <section class="py-12 bg-neutral-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="heading-2 text-center mb-8">Current Promotions</h2>
        <div class="grid md:grid-cols-3 gap-6">
          <div class="card relative overflow-hidden">
            <div class="promo-badge">Save $0.10</div>
            <NuxtImg 
              src="/drinks.webp" 
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
    </section> -->

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
        <h2 class="heading-2 text-center mb-12">Our Services</h2>
        <div class="grid md:grid-cols-4 gap-6">
          <div class="text-center">
            <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z"></path>
              </svg>
            </div>
            <h3 class="heading-4 mb-2">Fuel</h3>
            <p class="text-neutral-600">Quality gasoline and diesel fuel available 24/7.</p>
          </div>
          
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
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
              </svg>
            </div>
            <h3 class="heading-4 mb-2">Fresh Food</h3>
            <p class="text-neutral-600">Hot food, snacks, and beverages available.</p>
          </div>
          
          <div class="text-center">
            <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path>
              </svg>
            </div>
            <h3 class="heading-4 mb-2">Liquor & Spirits</h3>
            <p class="text-neutral-600">Wide selection of beer, wine, and spirits.</p>
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
              <div class="mb-4">
                <iframe 
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2805.4882811108355!2d-93.18742019999999!3d45.318761599999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x52b31e8fd36cf5ef%3A0xb2626555f4804002!2sGo%20For%20It%20Gas!5e0!3m2!1sen!2sca!4v1758335989282!5m2!1sen!2sca" 
                  width="100%" 
                  height="256" 
                  style="border:0;" 
                  allowfullscreen="" 
                  loading="lazy" 
                  referrerpolicy="no-referrer-when-downgrade"
                  class="rounded-lg"
                ></iframe>
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
