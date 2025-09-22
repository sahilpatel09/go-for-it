<template>
  <div>
    <!-- Hero Section -->
    <section class="relative h-96 flex items-center justify-center overflow-hidden">
      <div class="absolute inset-0">
        <NuxtImg 
          src="/images/backgrounds/services-background.webp" 
          alt="Go For It Liquor - Premium Spirits Destination"
          class="w-full h-full object-cover opacity-30"
        />
        <div class="absolute inset-0 bg-gradient-to-b from-black/60 via-black/40 to-black/80"></div>
      </div>
      <div class="relative z-10 text-center text-white max-w-4xl mx-auto px-4">
        <h1 class="text-5xl md:text-6xl font-bold mb-6" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">About Go For It Liquor</h1>
        <div class="w-24 h-1 bg-gradient-to-r from-transparent via-#D4AF37 to-transparent mx-auto mb-6"></div>
        <p class="text-xl md:text-2xl" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">Serving our community with premium spirits and exceptional service since 2004</p>
      </div>
    </section>

    <!-- Our Story -->
    <section class="py-20" style="background-color: #0A0A0A;">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-4xl font-bold mb-6" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Our Story</h2>
          <div class="w-24 h-1 bg-gradient-to-r from-transparent via-#D4AF37 to-transparent mx-auto mb-6"></div>
          <p class="text-xl" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
            Go For It Liquor has been a cornerstone of our community for over 20 years, 
            providing premium spirits, quality products, and exceptional service to thousands of customers.
          </p>
        </div>

        <div class="prose prose-lg max-w-none">
          <div class="rounded-2xl shadow-2xl p-8 mb-8" style="background-color: #1A1A1A;">
            <h3 class="text-2xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">From Humble Beginnings</h3>
            <p class="mb-4" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
              What started as a small family business in 2004 has grown into a trusted local establishment 
              that serves thousands of customers each week. Our founders, the Johnson family, had a simple 
              vision: to provide premium spirits and convenience store items with exceptional customer service.
            </p>
            <p class="mb-4" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
              Over the years, we've expanded our services to include car wash facilities, ATM services, 
              EV charging stations, and a wide variety of fresh food and beverages. But one thing has 
              never changed – our commitment to treating every customer like family.
            </p>
          </div>

          <div class="rounded-2xl shadow-2xl p-8 mb-8" style="background-color: #1A1A1A;">
            <h3 class="text-2xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Our Mission</h3>
            <p class="mb-4" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
              At Go For It Liquor, our mission is simple: to be your trusted neighborhood spirits destination, 
              providing premium spirits, fresh food, and essential services with a smile. We believe that 
              every interaction matters and strive to make your visit convenient, pleasant, and memorable.
            </p>
            <div class="grid md:grid-cols-3 gap-6 mt-6">
              <div class="text-center">
                <div class="w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4" style="background-color: rgba(212, 175, 55, 0.1);">
                  <svg class="w-8 h-8" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path>
                  </svg>
                </div>
                <h4 class="font-semibold mb-2" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Quality Service</h4>
                <p class="text-sm" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">We believe in treating every customer with respect and providing the best service possible.</p>
              </div>
              <div class="text-center">
                <div class="w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4" style="background-color: rgba(212, 175, 55, 0.1);">
                  <svg class="w-8 h-8" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path>
                  </svg>
                </div>
                <h4 class="font-semibold mb-2" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Community Focus</h4>
                <p class="text-sm" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">We're proud to be part of this community and support local events and organizations.</p>
              </div>
              <div class="text-center">
                <div class="w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4" style="background-color: rgba(212, 175, 55, 0.1);">
                  <svg class="w-8 h-8" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"></path>
                  </svg>
                </div>
                <h4 class="font-semibold mb-2" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Fair Pricing</h4>
                <p class="text-sm" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">We offer competitive prices on all our products without compromising on quality.</p>
              </div>
            </div>
          </div>

          <div class="rounded-2xl shadow-2xl p-8 mb-8" style="background-color: #1A1A1A;">
            <h3 class="text-2xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">What We Offer</h3>
            <div class="grid md:grid-cols-2 gap-6">
              <div>
                <h4 class="font-semibold mb-3" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Premium Spirits</h4>
                <ul class="space-y-2" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
                  <li class="flex items-start">
                    <div class="w-2 h-2 rounded-full mr-3 mt-2" style="background-color: #D4AF37;"></div>
                    <span>Premium whiskey, vodka, rum, and tequila</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 rounded-full mr-3 mt-2" style="background-color: #D4AF37;"></div>
                    <span>Curated wine selection</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 rounded-full mr-3 mt-2" style="background-color: #D4AF37;"></div>
                    <span>Craft beer and specialty beverages</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 rounded-full mr-3 mt-2" style="background-color: #D4AF37;"></div>
                    <span>Expert recommendations and tastings</span>
                  </li>
                </ul>
              </div>
              <div>
                <h4 class="font-semibold mb-3" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Convenience Store</h4>
                <ul class="space-y-2" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
                  <li class="flex items-start">
                    <div class="w-2 h-2 rounded-full mr-3 mt-2" style="background-color: #D4AF37;"></div>
                    <span>Fresh coffee and hot food</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 rounded-full mr-3 mt-2" style="background-color: #D4AF37;"></div>
                    <span>Snacks, drinks, and essentials</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 rounded-full mr-3 mt-2" style="background-color: #D4AF37;"></div>
                    <span>Tobacco products and lottery</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 rounded-full mr-3 mt-2" style="background-color: #D4AF37;"></div>
                    <span>ATM and financial services</span>
                  </li>
                </ul>
              </div>
            </div>
          </div>

          <div class="rounded-2xl shadow-2xl p-8" style="background-color: #1A1A1A;">
            <h3 class="text-2xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Additional Services</h3>
            <div class="grid md:grid-cols-2 gap-6">
              <div>
                <h4 class="font-semibold mb-3" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Automotive Services</h4>
                <ul class="space-y-2" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
                  <li class="flex items-start">
                    <div class="w-2 h-2 rounded-full mr-3 mt-2" style="background-color: #D4AF37;"></div>
                    <span>Professional car wash</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 rounded-full mr-3 mt-2" style="background-color: #D4AF37;"></div>
                    <span>Oil change services</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 rounded-full mr-3 mt-2" style="background-color: #D4AF37;"></div>
                    <span>Tire repair and maintenance</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 rounded-full mr-3 mt-2" style="background-color: #D4AF37;"></div>
                    <span>Free air and water</span>
                  </li>
                </ul>
              </div>
              <div>
                <h4 class="font-semibold mb-3" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Community Involvement</h4>
                <ul class="space-y-2" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
                  <li class="flex items-start">
                    <div class="w-2 h-2 rounded-full mr-3 mt-2" style="background-color: #D4AF37;"></div>
                    <span>Local school sponsorships</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 rounded-full mr-3 mt-2" style="background-color: #D4AF37;"></div>
                    <span>Community event support</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 rounded-full mr-3 mt-2" style="background-color: #D4AF37;"></div>
                    <span>Charitable donations</span>
                  </li>
                  <li class="flex items-start">
                    <div class="w-2 h-2 rounded-full mr-3 mt-2" style="background-color: #D4AF37;"></div>
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
    <section class="py-20" style="background-color: #0F0F0F;">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-4xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Our Journey</h2>
          <div class="w-24 h-1 bg-gradient-to-r from-transparent via-#D4AF37 to-transparent mx-auto mb-6"></div>
          <p class="text-xl" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">Key milestones in our 20+ year history</p>
        </div>

        <div class="space-y-8">
          <div class="flex items-start">
            <div class="w-12 h-12 rounded-full flex items-center justify-center mr-6 flex-shrink-0" style="background-color: #D4AF37;">
              <span class="font-bold" style="color: #0A0A0A;">2004</span>
            </div>
            <div class="rounded-lg p-6 shadow-2xl" style="background-color: #1A1A1A;">
              <h3 class="text-xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Grand Opening</h3>
              <p style="color: #E5E5E5; font-family: 'Inter', sans-serif;">Go For It Liquor opened its doors as a small family-owned spirits destination with basic convenience store items.</p>
            </div>
          </div>

          <div class="flex items-start">
            <div class="w-12 h-12 rounded-full flex items-center justify-center mr-6 flex-shrink-0" style="background-color: #D4AF37;">
              <span class="font-bold" style="color: #0A0A0A;">2008</span>
            </div>
            <div class="rounded-lg p-6 shadow-2xl" style="background-color: #1A1A1A;">
              <h3 class="text-xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Expansion</h3>
              <p style="color: #E5E5E5; font-family: 'Inter', sans-serif;">Added car wash facilities and expanded the convenience store to offer fresh food and hot beverages.</p>
            </div>
          </div>

          <div class="flex items-start">
            <div class="w-12 h-12 rounded-full flex items-center justify-center mr-6 flex-shrink-0" style="background-color: #D4AF37;">
              <span class="font-bold" style="color: #0A0A0A;">2015</span>
            </div>
            <div class="rounded-lg p-6 shadow-2xl" style="background-color: #1A1A1A;">
              <h3 class="text-xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Modernization</h3>
              <p style="color: #E5E5E5; font-family: 'Inter', sans-serif;">Upgraded fuel pumps, added ATM services, and introduced loyalty rewards program.</p>
            </div>
          </div>

          <div class="flex items-start">
            <div class="w-12 h-12 rounded-full flex items-center justify-center mr-6 flex-shrink-0" style="background-color: #D4AF37;">
              <span class="font-bold" style="color: #0A0A0A;">2020</span>
            </div>
            <div class="rounded-lg p-6 shadow-2xl" style="background-color: #1A1A1A;">
              <h3 class="text-xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">EV Charging</h3>
              <p style="color: #E5E5E5; font-family: 'Inter', sans-serif;">Installed electric vehicle charging stations to serve the growing number of EV drivers in our community.</p>
            </div>
          </div>

          <div class="flex items-start">
            <div class="w-12 h-12 rounded-full flex items-center justify-center mr-6 flex-shrink-0" style="background-color: #D4AF37;">
              <span class="font-bold" style="color: #0A0A0A;">2024</span>
            </div>
            <div class="rounded-lg p-6 shadow-2xl" style="background-color: #1A1A1A;">
              <h3 class="text-xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">20th Anniversary</h3>
              <p style="color: #E5E5E5; font-family: 'Inter', sans-serif;">Celebrating 20 years of serving our community with expanded services and continued commitment to excellence.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Team Section -->
    <section class="py-20" style="background-color: #0A0A0A;">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-4xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Meet Our Team</h2>
          <div class="w-24 h-1 bg-gradient-to-r from-transparent via-#D4AF37 to-transparent mx-auto mb-6"></div>
          <p class="text-xl" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">The friendly faces behind Go For It Liquor</p>
        </div>

        <div class="grid md:grid-cols-3 gap-8">
          <div class="text-center">
            <div class="w-32 h-32 rounded-full mx-auto mb-4 flex items-center justify-center" style="background-color: rgba(212, 175, 55, 0.1);">
              <svg class="w-16 h-16" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
              </svg>
            </div>
            <h3 class="text-xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Mike Johnson</h3>
            <p class="font-medium mb-2" style="color: #D4AF37; font-family: 'Inter', sans-serif;">Owner & Manager</p>
            <p class="text-sm" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">Founded Go For It Liquor in 2004 with a vision to serve the community with premium spirits and friendly service.</p>
          </div>

          <div class="text-center">
            <div class="w-32 h-32 rounded-full mx-auto mb-4 flex items-center justify-center" style="background-color: rgba(212, 175, 55, 0.1);">
              <svg class="w-16 h-16" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
              </svg>
            </div>
            <h3 class="text-xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Sarah Martinez</h3>
            <p class="font-medium mb-2" style="color: #D4AF37; font-family: 'Inter', sans-serif;">Assistant Manager</p>
            <p class="text-sm" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">Manages daily operations and ensures every customer receives exceptional service during their visit.</p>
          </div>

          <div class="text-center">
            <div class="w-32 h-32 rounded-full mx-auto mb-4 flex items-center justify-center" style="background-color: rgba(212, 175, 55, 0.1);">
              <svg class="w-16 h-16" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
              </svg>
            </div>
            <h3 class="text-xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Tom Wilson</h3>
            <p class="font-medium mb-2" style="color: #D4AF37; font-family: 'Inter', sans-serif;">Service Technician</p>
            <p class="text-sm" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">Expert in automotive services including oil changes, tire repair, and car wash maintenance.</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
useHead({
  title: 'About Us - Go For It Liquor',
  meta: [
    { name: 'description', content: 'Learn about Go For It Liquor, serving our community since 2004. Our story, mission, and commitment to premium spirits and exceptional service.' },
    { name: 'keywords', content: 'about us, company history, team, mission, values, community service, East Bethel, premium spirits, liquor store' }
  ]
})
</script>
