<template>
  <div>
    <!-- Hero Section -->
    <section class="relative h-64 flex items-center justify-center overflow-hidden">
      <div class="absolute inset-0">
        <NuxtImg 
          src="/images/about-hero.jpg" 
          alt="Go For It Gas team and exterior"
          class="w-full h-full object-cover"
        />
        <div class="hero-overlay"></div>
      </div>
      <div class="relative z-10 text-center text-white">
        <h1 class="heading-2 mb-4 text-shadow-lg">About Go For It Gas</h1>
        <p class="text-lg text-shadow">Serving our community with pride since 2004</p>
      </div>
    </section>

    <!-- Our Story -->
    <section class="py-16">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="heading-2 mb-6">Our Story</h2>
          <p class="text-xl text-neutral-600">
            Go For It Gas has been a cornerstone of our community for over 20 years, 
            providing reliable fuel, quality products, and friendly service to thousands of customers.
          </p>
        </div>

        <div class="prose prose-lg max-w-none">
          <div class="bg-white rounded-xl shadow-soft p-8 mb-8">
            <h3 class="heading-3 mb-4">From Humble Beginnings</h3>
            <p class="text-neutral-700 mb-4">
              What started as a small family business in 2004 has grown into a trusted local establishment 
              that serves thousands of customers each week. Our founders, the Johnson family, had a simple 
              vision: to provide quality fuel and convenience store items with exceptional customer service.
            </p>
            <p class="text-neutral-700 mb-4">
              Over the years, we've expanded our services to include car wash facilities, ATM services, 
              EV charging stations, and a wide variety of fresh food and beverages. But one thing has 
              never changed – our commitment to treating every customer like family.
            </p>
          </div>

          <div class="bg-white rounded-xl shadow-soft p-8 mb-8">
            <h3 class="heading-3 mb-4">Our Mission</h3>
            <p class="text-neutral-700 mb-4">
              At Go For It Gas, our mission is simple: to be your trusted neighborhood service station, 
              providing quality fuel, fresh food, and essential services with a smile. We believe that 
              every interaction matters and strive to make your visit convenient, pleasant, and memorable.
            </p>
            <div class="grid md:grid-cols-3 gap-6 mt-6">
              <div class="text-center">
                <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
                  <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path>
                  </svg>
                </div>
                <h4 class="font-semibold text-neutral-900 mb-2">Quality Service</h4>
                <p class="text-sm text-neutral-600">We believe in treating every customer with respect and providing the best service possible.</p>
              </div>
              <div class="text-center">
                <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
                  <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path>
                  </svg>
                </div>
                <h4 class="font-semibold text-neutral-900 mb-2">Community Focus</h4>
                <p class="text-sm text-neutral-600">We're proud to be part of this community and support local events and organizations.</p>
              </div>
              <div class="text-center">
                <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
                  <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"></path>
                  </svg>
                </div>
                <h4 class="font-semibold text-neutral-900 mb-2">Fair Pricing</h4>
                <p class="text-sm text-neutral-600">We offer competitive prices on all our products without compromising on quality.</p>
              </div>
            </div>
          </div>

          <div class="bg-white rounded-xl shadow-soft p-8 mb-8">
            <h3 class="heading-3 mb-4">What We Offer</h3>
            <div class="grid md:grid-cols-2 gap-6">
              <div>
                <h4 class="font-semibold text-neutral-900 mb-3">Fuel Services</h4>
                <ul class="text-neutral-700 space-y-2">
                  <li class="flex items-start">
                    <div class="w-2 h-2 bg-primary-500 rounded-full mr-3 mt-2"></div>
                    <span>Regular, Plus, Premium, and Diesel fuel</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 bg-primary-500 rounded-full mr-3 mt-2"></div>
                    <span>24/7 gas pump access</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 bg-primary-500 rounded-full mr-3 mt-2"></div>
                    <span>Competitive daily pricing</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 bg-primary-500 rounded-full mr-3 mt-2"></div>
                    <span>EV charging stations</span>
                  </li>
                </ul>
              </div>
              <div>
                <h4 class="font-semibold text-neutral-900 mb-3">Convenience Store</h4>
                <ul class="text-neutral-700 space-y-2">
                  <li class="flex items-start">
                    <div class="w-2 h-2 bg-primary-500 rounded-full mr-3 mt-2"></div>
                    <span>Fresh coffee and hot food</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 bg-primary-500 rounded-full mr-3 mt-2"></div>
                    <span>Snacks, drinks, and essentials</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 bg-primary-500 rounded-full mr-3 mt-2"></div>
                    <span>Tobacco products and lottery</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 bg-primary-500 rounded-full mr-3 mt-2"></div>
                    <span>ATM and financial services</span>
                  </li>
                </ul>
              </div>
            </div>
          </div>

          <div class="bg-white rounded-xl shadow-soft p-8">
            <h3 class="heading-3 mb-4">Additional Services</h3>
            <div class="grid md:grid-cols-2 gap-6">
              <div>
                <h4 class="font-semibold text-neutral-900 mb-3">Automotive Services</h4>
                <ul class="text-neutral-700 space-y-2">
                  <li class="flex items-start">
                    <div class="w-2 h-2 bg-primary-500 rounded-full mr-3 mt-2"></div>
                    <span>Professional car wash</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 bg-primary-500 rounded-full mr-3 mt-2"></div>
                    <span>Oil change services</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 bg-primary-500 rounded-full mr-3 mt-2"></div>
                    <span>Tire repair and maintenance</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 bg-primary-500 rounded-full mr-3 mt-2"></div>
                    <span>Free air and water</span>
                  </li>
                </ul>
              </div>
              <div>
                <h4 class="font-semibold text-neutral-900 mb-3">Community Involvement</h4>
                <ul class="text-neutral-700 space-y-2">
                  <li class="flex items-start">
                    <div class="w-2 h-2 bg-primary-500 rounded-full mr-3 mt-2"></div>
                    <span>Local school sponsorships</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 bg-primary-500 rounded-full mr-3 mt-2"></div>
                    <span>Community event support</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 bg-primary-500 rounded-full mr-3 mt-2"></div>
                    <span>Charitable donations</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 bg-primary-500 rounded-full mr-3 mt-2"></div>
                    <span>Local business partnerships</span>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Timeline -->
    <section class="py-16 bg-neutral-50">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="heading-2 mb-4">Our Journey</h2>
          <p class="text-xl text-neutral-600">Key milestones in our 20+ year history</p>
        </div>

        <div class="space-y-8">
          <div class="flex items-start">
            <div class="w-12 h-12 bg-primary-500 rounded-full flex items-center justify-center mr-6 flex-shrink-0">
              <span class="text-white font-bold">2004</span>
            </div>
            <div class="bg-white rounded-lg p-6 shadow-soft">
              <h3 class="heading-4 mb-2">Grand Opening</h3>
              <p class="text-neutral-600">Go For It Gas opened its doors as a small family-owned gas station with basic convenience store items.</p>
            </div>
          </div>

          <div class="flex items-start">
            <div class="w-12 h-12 bg-primary-500 rounded-full flex items-center justify-center mr-6 flex-shrink-0">
              <span class="text-white font-bold">2008</span>
            </div>
            <div class="bg-white rounded-lg p-6 shadow-soft">
              <h3 class="heading-4 mb-2">Expansion</h3>
              <p class="text-neutral-600">Added car wash facilities and expanded the convenience store to offer fresh food and hot beverages.</p>
            </div>
          </div>

          <div class="flex items-start">
            <div class="w-12 h-12 bg-primary-500 rounded-full flex items-center justify-center mr-6 flex-shrink-0">
              <span class="text-white font-bold">2015</span>
            </div>
            <div class="bg-white rounded-lg p-6 shadow-soft">
              <h3 class="heading-4 mb-2">Modernization</h3>
              <p class="text-neutral-600">Upgraded fuel pumps, added ATM services, and introduced loyalty rewards program.</p>
            </div>
          </div>

          <div class="flex items-start">
            <div class="w-12 h-12 bg-primary-500 rounded-full flex items-center justify-center mr-6 flex-shrink-0">
              <span class="text-white font-bold">2020</span>
            </div>
            <div class="bg-white rounded-lg p-6 shadow-soft">
              <h3 class="heading-4 mb-2">EV Charging</h3>
              <p class="text-neutral-600">Installed electric vehicle charging stations to serve the growing number of EV drivers in our community.</p>
            </div>
          </div>

          <div class="flex items-start">
            <div class="w-12 h-12 bg-primary-500 rounded-full flex items-center justify-center mr-6 flex-shrink-0">
              <span class="text-white font-bold">2024</span>
            </div>
            <div class="bg-white rounded-lg p-6 shadow-soft">
              <h3 class="heading-4 mb-2">20th Anniversary</h3>
              <p class="text-neutral-600">Celebrating 20 years of serving our community with expanded services and continued commitment to excellence.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Team Section -->
    <section class="py-16">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="heading-2 mb-4">Meet Our Team</h2>
          <p class="text-xl text-neutral-600">The friendly faces behind Go For It Gas</p>
        </div>

        <div class="grid md:grid-cols-3 gap-8">
          <div class="text-center">
            <div class="w-32 h-32 bg-neutral-200 rounded-full mx-auto mb-4 flex items-center justify-center">
              <svg class="w-16 h-16 text-neutral-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
              </svg>
            </div>
            <h3 class="heading-4 mb-2">Mike Johnson</h3>
            <p class="text-primary-600 font-medium mb-2">Owner & Manager</p>
            <p class="text-sm text-neutral-600">Founded Go For It Gas in 2004 with a vision to serve the community with quality fuel and friendly service.</p>
          </div>

          <div class="text-center">
            <div class="w-32 h-32 bg-neutral-200 rounded-full mx-auto mb-4 flex items-center justify-center">
              <svg class="w-16 h-16 text-neutral-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
              </svg>
            </div>
            <h3 class="heading-4 mb-2">Sarah Martinez</h3>
            <p class="text-primary-600 font-medium mb-2">Assistant Manager</p>
            <p class="text-sm text-neutral-600">Manages daily operations and ensures every customer receives exceptional service during their visit.</p>
          </div>

          <div class="text-center">
            <div class="w-32 h-32 bg-neutral-200 rounded-full mx-auto mb-4 flex items-center justify-center">
              <svg class="w-16 h-16 text-neutral-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
              </svg>
            </div>
            <h3 class="heading-4 mb-2">Tom Wilson</h3>
            <p class="text-primary-600 font-medium mb-2">Service Technician</p>
            <p class="text-sm text-neutral-600">Expert in automotive services including oil changes, tire repair, and car wash maintenance.</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
useHead({
  title: 'About Us - Go For It Gas',
  meta: [
    { name: 'description', content: 'Learn about Go For It Gas, serving our community since 2004. Our story, mission, and commitment to quality fuel and friendly service.' },
    { name: 'keywords', content: 'about us, company history, team, mission, values, community service, East Bethel' }
  ]
})
</script>
