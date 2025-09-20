<template>
  <div>
    <!-- Hero Section -->
    <section class="relative h-80 flex items-center justify-center overflow-hidden bg-gradient-to-br from-slate-900 via-slate-800 to-amber-900">
      <div class="absolute inset-0">
        <NuxtImg 
          src="/test_image.jpg" 
          alt="Go For It Liquor Store Interior"
          class="w-full h-full object-cover opacity-30"
        />
        <div class="absolute inset-0 bg-gradient-to-br from-slate-900/80 via-slate-800/70 to-amber-900/80"></div>
      </div>
      <div class="relative z-10 text-center text-white">
        <h1 class="text-4xl md:text-6xl font-bold mb-6 text-shadow-lg">Convenience Store</h1>
        <p class="text-xl md:text-2xl text-amber-100 text-shadow">Everything you need, right here</p>
      </div>
    </section>

    <!-- Store Highlights -->
    <section class="py-20 bg-slate-800">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-4xl md:text-5xl font-bold text-white mb-6">Why Stop at Go For It Liquor?</h2>
          <p class="text-xl text-slate-300 max-w-3xl mx-auto">
            Our convenience store offers a wide variety of fresh food, snacks, drinks, and everyday essentials. 
            We're committed to providing quick, friendly service and quality products at competitive prices.
          </p>
        </div>

        <!-- Product Categories -->
        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8 mb-16">
          <div class="bg-gradient-to-br from-amber-800 to-amber-700 rounded-2xl overflow-hidden shadow-xl hover:shadow-2xl transition-all duration-300 hover:scale-105">
            <div class="absolute top-4 right-4 z-10">
              <span class="bg-red-600 text-white px-3 py-1 rounded-full text-sm font-bold">Fresh Daily</span>
            </div>
            <NuxtImg 
              src="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" 
              alt="Fresh Coffee Selection"
              class="w-full h-48 object-cover"
            />
            <div class="p-6">
              <h3 class="text-xl font-bold text-white mb-3">Coffee & Hot Drinks</h3>
              <p class="text-amber-100 mb-4">Premium coffee blends, hot chocolate, tea, and specialty drinks.</p>
              <ul class="text-sm text-amber-200 space-y-1">
                <li>• Regular & Decaf Coffee</li>
                <li>• Espresso Drinks</li>
                <li>• Hot Chocolate</li>
                <li>• Tea Selection</li>
              </ul>
            </div>
          </div>

          <div class="bg-gradient-to-br from-red-800 to-red-700 rounded-2xl overflow-hidden shadow-xl hover:shadow-2xl transition-all duration-300 hover:scale-105">
            <div class="absolute top-4 right-4 z-10">
              <span class="bg-red-600 text-white px-3 py-1 rounded-full text-sm font-bold">Hot & Fresh</span>
            </div>
            <NuxtImg 
              src="https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" 
              alt="Hot Food Selection"
              class="w-full h-48 object-cover"
            />
            <div class="p-6">
              <h3 class="text-xl font-bold text-white mb-3">Hot Food</h3>
              <p class="text-red-100 mb-4">Fresh sandwiches, hot dogs, and daily specials made fresh.</p>
              <ul class="text-sm text-red-200 space-y-1">
                <li>• Fresh Sandwiches</li>
                <li>• Hot Dogs & Sausages</li>
                <li>• Pizza Slices</li>
                <li>• Daily Specials</li>
              </ul>
            </div>
          </div>

          <div class="bg-gradient-to-br from-slate-700 to-slate-600 rounded-2xl overflow-hidden shadow-xl hover:shadow-2xl transition-all duration-300 hover:scale-105">
            <div class="absolute top-4 right-4 z-10">
              <span class="bg-red-600 text-white px-3 py-1 rounded-full text-sm font-bold">Wide Selection</span>
            </div>
            <NuxtImg 
              src="https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" 
              alt="Snacks and Drinks"
              class="w-full h-48 object-cover"
            />
            <div class="p-6">
              <h3 class="text-xl font-bold text-white mb-3">Snacks & Drinks</h3>
              <p class="text-slate-200 mb-4">Chips, candy, cold beverages, and energy drinks.</p>
              <ul class="text-sm text-slate-300 space-y-1">
                <li>• Chips & Crackers</li>
                <li>• Candy & Chocolate</li>
                <li>• Cold Beverages</li>
                <li>• Energy Drinks</li>
              </ul>
            </div>
          </div>

          <div class="bg-gradient-to-br from-amber-700 to-amber-600 rounded-2xl overflow-hidden shadow-xl hover:shadow-2xl transition-all duration-300 hover:scale-105">
            <div class="absolute top-4 right-4 z-10">
              <span class="bg-red-600 text-white px-3 py-1 rounded-full text-sm font-bold">Daily Essentials</span>
            </div>
            <NuxtImg 
              src="https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" 
              alt="Daily Essentials"
              class="w-full h-48 object-cover"
            />
            <div class="p-6">
              <h3 class="text-xl font-bold text-white mb-3">Daily Essentials</h3>
              <p class="text-amber-100 mb-4">Tobacco products, lottery tickets, and everyday items.</p>
              <ul class="text-sm text-amber-200 space-y-1">
                <li>• Tobacco Products</li>
                <li>• Lottery Tickets</li>
                <li>• Basic Medications</li>
                <li>• Personal Care</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Featured Products -->
        <div class="bg-gradient-to-br from-slate-700 to-slate-600 rounded-2xl p-8">
          <h3 class="text-3xl font-bold text-white text-center mb-8">Featured Products</h3>
          <div class="grid md:grid-cols-3 gap-8">
            <div class="bg-slate-800 rounded-lg p-6 text-center hover:bg-slate-700 transition-colors duration-300">
              <div class="w-16 h-16 bg-gradient-to-br from-amber-600 to-amber-700 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path>
                </svg>
              </div>
              <h4 class="text-lg font-semibold text-white mb-2">Premium Coffee</h4>
              <p class="text-sm text-slate-300">Freshly brewed premium coffee available all day</p>
            </div>
            
            <div class="bg-slate-800 rounded-lg p-6 text-center hover:bg-slate-700 transition-colors duration-300">
              <div class="w-16 h-16 bg-gradient-to-br from-amber-600 to-amber-700 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
              </div>
              <h4 class="text-lg font-semibold text-white mb-2">Hot Food</h4>
              <p class="text-sm text-slate-300">Fresh sandwiches and hot food made daily</p>
            </div>
            
            <div class="bg-slate-800 rounded-lg p-6 text-center hover:bg-slate-700 transition-colors duration-300">
              <div class="w-16 h-16 bg-gradient-to-br from-amber-600 to-amber-700 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path>
                </svg>
              </div>
              <h4 class="text-lg font-semibold text-white mb-2">Cold Drinks</h4>
              <p class="text-sm text-slate-300">Wide selection of cold beverages and energy drinks</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Store Hours & Contact -->
    <section class="py-20 bg-gradient-to-br from-slate-900 to-slate-800">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center text-white">
        <h2 class="text-4xl md:text-5xl font-bold mb-8">Visit Our Store Today</h2>
        <div class="grid md:grid-cols-2 gap-8 mb-8">
          <div class="bg-slate-800 rounded-2xl p-8">
            <h3 class="text-2xl font-bold text-amber-400 mb-6">Store Hours</h3>
            <div class="space-y-3 text-left">
              <div class="flex justify-between py-2 border-b border-slate-700">
                <span class="text-white font-medium">Monday - Friday</span>
                <span class="text-slate-300">6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between py-2 border-b border-slate-700">
                <span class="text-white font-medium">Saturday</span>
                <span class="text-slate-300">6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between py-2">
                <span class="text-white font-medium">Sunday</span>
                <span class="text-slate-300">6:00 AM - 10:00 PM</span>
              </div>
            </div>
          </div>
          <div class="bg-slate-800 rounded-2xl p-8">
            <h3 class="text-2xl font-bold text-amber-400 mb-6">Contact Info</h3>
            <div class="space-y-4 text-left">
              <div class="flex items-center">
                <svg class="w-6 h-6 text-amber-500 mr-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                </svg>
                <span class="text-white">3255 Viking Blvd NE, East Bethel, MN 55092</span>
              </div>
              <div class="flex items-center">
                <svg class="w-6 h-6 text-amber-500 mr-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
                </svg>
                <a href="tel:+16513952174" class="text-white hover:text-amber-400 transition-colors">(651) 395-2174</a>
              </div>
            </div>
          </div>
        </div>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <a href="https://www.google.com/maps?cid=12853947706317488130" target="_blank" class="bg-amber-600 hover:bg-amber-700 text-white px-8 py-4 text-lg font-semibold rounded-lg shadow-lg hover:shadow-xl transition-all duration-300">
            Get Directions
          </a>
          <a href="tel:+16513952174" class="bg-transparent border-2 border-amber-400 text-amber-400 hover:bg-amber-400 hover:text-slate-900 px-8 py-4 text-lg font-semibold rounded-lg transition-all duration-300">
            Call Now
          </a>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
useHead({
  title: 'Convenience Store - Go For It Liquor',
  meta: [
    { name: 'description', content: 'Visit our convenience store for fresh coffee, hot food, snacks, drinks, and daily essentials. Open daily with friendly service in East Bethel, MN.' },
    { name: 'keywords', content: 'convenience store, coffee, hot food, snacks, drinks, tobacco, lottery, East Bethel, Minnesota' }
  ]
})
</script>
