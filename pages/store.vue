<template>
  <div>
    <!-- Hero Section -->
    <section class="relative h-64 flex items-center justify-center overflow-hidden">
      <div class="absolute inset-0">
        <NuxtImg 
          src="/img.webp" 
          alt="Go For It Gas Station - 3255 Viking Blvd NE, East Bethel, MN"
          class="w-full h-full object-cover"
        />
        <div class="hero-overlay"></div>
      </div>
      <div class="relative z-10 text-center text-white">
        <h1 class="heading-2 mb-4 text-shadow-lg text-white">Convenience Store</h1>
        <p class="text-lg text-shadow">Everything you need, right here</p>
      </div>
    </section>

    <!-- Store Highlights -->
    <section class="py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="heading-2 mb-4">Why Stop at Go For It Gas?</h2>
          <p class="text-xl text-neutral-600 max-w-3xl mx-auto">
            Our convenience store offers a wide variety of fresh food, snacks, drinks, and everyday essentials. 
            We're committed to providing quick, friendly service and quality products at competitive prices.
          </p>
        </div>

        <!-- Product Categories -->
        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
          <div class="card relative overflow-hidden">
            <div class="promo-badge">Fresh Daily</div>
            <NuxtImg 
              src="/images/coffee-products.jpg" 
              alt="Fresh Coffee Selection"
              class="w-full h-48 object-cover"
            />
            <div class="card-body">
              <h3 class="heading-4 mb-2">Coffee & Hot Drinks</h3>
              <p class="text-neutral-600 mb-4">Premium coffee blends, hot chocolate, tea, and specialty drinks.</p>
              <ul class="text-sm text-neutral-600 space-y-1">
                <li>• Regular & Decaf Coffee</li>
                <li>• Espresso Drinks</li>
                <li>• Hot Chocolate</li>
                <li>• Tea Selection</li>
              </ul>
            </div>
          </div>

          <div class="card relative overflow-hidden">
            <div class="promo-badge">Hot & Fresh</div>
            <NuxtImg 
              src="/images/hot-food.jpg" 
              alt="Hot Food Selection"
              class="w-full h-48 object-cover"
            />
            <div class="card-body">
              <h3 class="heading-4 mb-2">Hot Food</h3>
              <p class="text-neutral-600 mb-4">Fresh sandwiches, hot dogs, and daily specials made fresh.</p>
              <ul class="text-sm text-neutral-600 space-y-1">
                <li>• Fresh Sandwiches</li>
                <li>• Hot Dogs & Sausages</li>
                <li>• Pizza Slices</li>
                <li>• Daily Specials</li>
              </ul>
            </div>
          </div>

          <div class="card relative overflow-hidden">
            <div class="promo-badge">Wide Selection</div>
            <NuxtImg 
              src="/images/snacks-drinks.jpg" 
              alt="Snacks and Drinks"
              class="w-full h-48 object-cover"
            />
            <div class="card-body">
              <h3 class="heading-4 mb-2">Snacks & Drinks</h3>
              <p class="text-neutral-600 mb-4">Chips, candy, cold beverages, and energy drinks.</p>
              <ul class="text-sm text-neutral-600 space-y-1">
                <li>• Chips & Crackers</li>
                <li>• Candy & Chocolate</li>
                <li>• Cold Beverages</li>
                <li>• Energy Drinks</li>
              </ul>
            </div>
          </div>

          <div class="card relative overflow-hidden">
            <div class="promo-badge">Daily Essentials</div>
            <NuxtImg 
              src="/images/essentials.jpg" 
              alt="Daily Essentials"
              class="w-full h-48 object-cover"
            />
            <div class="card-body">
              <h3 class="heading-4 mb-2">Daily Essentials</h3>
              <p class="text-neutral-600 mb-4">Tobacco products, lottery tickets, and everyday items.</p>
              <ul class="text-sm text-neutral-600 space-y-1">
                <li>• Tobacco Products</li>
                <li>• Lottery Tickets</li>
                <li>• Basic Medications</li>
                <li>• Personal Care</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Featured Products -->
        <div class="bg-neutral-50 rounded-xl p-8">
          <h3 class="heading-3 text-center mb-8">Featured Products</h3>
          <div class="grid md:grid-cols-3 gap-6">
            <div class="bg-white rounded-lg p-6 text-center">
              <div class="w-12 h-12 bg-accent-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-6 h-6 text-accent-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path>
                </svg>
              </div>
              <h4 class="font-semibold mb-2">Premium Coffee</h4>
              <p class="text-sm text-neutral-600">Freshly brewed premium coffee available all day</p>
            </div>
            
            <div class="bg-white rounded-lg p-6 text-center">
              <div class="w-12 h-12 bg-accent-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-6 h-6 text-accent-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
              </div>
              <h4 class="font-semibold mb-2">Hot Food</h4>
              <p class="text-sm text-neutral-600">Fresh sandwiches and hot food made daily</p>
            </div>
            
            <div class="bg-white rounded-lg p-6 text-center">
              <div class="w-12 h-12 bg-accent-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-6 h-6 text-accent-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path>
                </svg>
              </div>
              <h4 class="font-semibold mb-2">Cold Drinks</h4>
              <p class="text-sm text-neutral-600">Wide selection of cold beverages and energy drinks</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Store Hours & Contact -->
    <section class="py-16 bg-primary-500">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center text-white">
        <h2 class="heading-2 mb-8">Visit Our Store Today</h2>
        <div class="grid md:grid-cols-2 gap-8 mb-8">
          <div>
            <h3 class="heading-4 mb-4">Store Hours</h3>
            <div class="space-y-2 text-left">
              <div class="flex justify-between">
                <span>Monday - Friday</span>
                <span>6:00 AM - 11:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span>Saturday</span>
                <span>7:00 AM - 11:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span>Sunday</span>
                <span>8:00 AM - 10:00 PM</span>
              </div>
            </div>
          </div>
          <div>
            <h3 class="heading-4 mb-4">Contact Info</h3>
            <div class="space-y-2 text-left">
              <div class="flex items-center">
                <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                </svg>
                <span>3255 Viking Blvd NE, East Bethel, MN 55092</span>
              </div>
              <div class="flex items-center">
                <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
                </svg>
                <a href="tel:+15551234567" class="hover:text-accent-300 transition-colors">(555) 123-4567</a>
              </div>
            </div>
          </div>
        </div>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <a href="https://www.google.com/maps?cid=12853947706317488130" target="_blank" class="btn-secondary">
            Get Directions
          </a>
          <a href="tel:+16513952174" class="btn-outline border-white text-white hover:bg-white hover:text-primary-500">
            Call Now
          </a>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
useHead({
  title: 'Convenience Store - Go For It Gas',
  meta: [
    { name: 'description', content: 'Visit our convenience store for fresh coffee, hot food, snacks, drinks, and daily essentials. Open daily with friendly service.' },
    { name: 'keywords', content: 'convenience store, coffee, hot food, snacks, drinks, tobacco, lottery, East Bethel' }
  ]
})
</script>
