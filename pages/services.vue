<template>
  <div>
    <!-- Hero Section -->
    <section class="relative h-96 flex items-center justify-center overflow-hidden">
      <div class="absolute inset-0">
        <NuxtImg 
          src="/img.webp" 
          alt="Go For It Liquor - Premium Services"
          class="w-full h-full object-cover opacity-30"
        />
        <div class="absolute inset-0 bg-gradient-to-b from-black/60 via-black/40 to-black/80"></div>
      </div>
      <div class="relative z-10 text-center text-white max-w-4xl mx-auto px-4">
        <h1 class="text-5xl md:text-6xl font-bold mb-6" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Premium Services</h1>
        <div class="w-24 h-1 bg-gradient-to-r from-transparent via-#D4AF37 to-transparent mx-auto mb-6"></div>
        <p class="text-xl md:text-2xl" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">More than just spirits - we're your complete service destination</p>
      </div>
    </section>

    <!-- Services Grid -->
    <section class="py-20" style="background-color: #0A0A0A;">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-4xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Our Services</h2>
          <div class="w-24 h-1 bg-gradient-to-r from-transparent via-#D4AF37 to-transparent mx-auto mb-6"></div>
          <p class="text-xl max-w-3xl mx-auto" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
            Beyond premium spirits, we offer a range of services to make your visit convenient and complete. 
            From car care to financial services, we've got you covered.
          </p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Car Wash -->
          <div class="rounded-2xl shadow-2xl p-8" style="background-color: #1A1A1A;">
            <div class="text-center">
              <div class="w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-6" style="background-color: rgba(212, 175, 55, 0.1);">
                <svg class="w-10 h-10" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
                </svg>
              </div>
              <h3 class="text-2xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Car Wash</h3>
              <p class="mb-6" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
                Professional car wash services to keep your vehicle looking its best. 
                Choose from basic wash to premium detailing packages.
              </p>
              <div class="space-y-2 text-sm mb-6" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                <div class="flex justify-between">
                  <span>Basic Wash</span>
                  <span style="color: #D4AF37;">$8.00</span>
                </div>
                <div class="flex justify-between">
                  <span>Premium Wash</span>
                  <span style="color: #D4AF37;">$12.00</span>
                </div>
                <div class="flex justify-between">
                  <span>Full Detail</span>
                  <span style="color: #D4AF37;">$25.00</span>
                </div>
              </div>
              <button class="w-full py-3 px-6 rounded-lg font-medium transition-all duration-300" style="background-color: #D4AF37; color: #0A0A0A; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#E5C547';" onmouseout="this.style.backgroundColor='#D4AF37';">Book Service</button>
            </div>
          </div>

          <!-- ATM -->
          <div class="rounded-2xl shadow-2xl p-8" style="background-color: #1A1A1A;">
            <div class="text-center">
              <div class="w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-6" style="background-color: rgba(212, 175, 55, 0.1);">
                <svg class="w-10 h-10" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"></path>
                </svg>
              </div>
              <h3 class="text-2xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">ATM Services</h3>
              <p class="mb-6" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
                24/7 ATM access for your banking needs. Withdraw cash, check balances, 
                and manage your accounts conveniently.
              </p>
              <div class="space-y-2 text-sm mb-6" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                <div class="flex justify-between">
                  <span>Cash Withdrawal</span>
                  <span style="color: #D4AF37;">Available</span>
                </div>
                <div class="flex justify-between">
                  <span>Balance Inquiry</span>
                  <span style="color: #D4AF37;">Free</span>
                </div>
                <div class="flex justify-between">
                  <span>Deposit</span>
                  <span style="color: #D4AF37;">Available</span>
                </div>
              </div>
              <button class="w-full py-3 px-6 rounded-lg font-medium transition-all duration-300" style="background-color: #D4AF37; color: #0A0A0A; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#E5C547';" onmouseout="this.style.backgroundColor='#D4AF37';">Find ATM</button>
            </div>
          </div>

          <!-- Air & Water -->
          <div class="rounded-2xl shadow-2xl p-8" style="background-color: #1A1A1A;">
            <div class="text-center">
              <div class="w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-6" style="background-color: rgba(212, 175, 55, 0.1);">
                <svg class="w-10 h-10" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 10-9.78 2.096A4.001 4.001 0 003 15z"></path>
                </svg>
              </div>
              <h3 class="text-2xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Air & Water</h3>
              <p class="mb-6" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
                Free air for your tires and water for your radiator. 
                Keep your vehicle running smoothly with our complimentary services.
              </p>
              <div class="space-y-2 text-sm mb-6" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                <div class="flex justify-between">
                  <span>Tire Air</span>
                  <span style="color: #D4AF37;">Free</span>
                </div>
                <div class="flex justify-between">
                  <span>Radiator Water</span>
                  <span style="color: #D4AF37;">Free</span>
                </div>
                <div class="flex justify-between">
                  <span>Windshield Fluid</span>
                  <span style="color: #D4AF37;">$2.00</span>
                </div>
              </div>
              <button class="w-full py-3 px-6 rounded-lg font-medium transition-all duration-300" style="background-color: #D4AF37; color: #0A0A0A; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#E5C547';" onmouseout="this.style.backgroundColor='#D4AF37';">Get Service</button>
            </div>
          </div>

          <!-- EV Charging -->
          <div class="rounded-2xl shadow-2xl p-8" style="background-color: #1A1A1A;">
            <div class="text-center">
              <div class="w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-6" style="background-color: rgba(212, 175, 55, 0.1);">
                <svg class="w-10 h-10" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
                </svg>
              </div>
              <h3 class="text-2xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">EV Charging</h3>
              <p class="mb-6" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
                Electric vehicle charging stations available for modern drivers. 
                Fast charging options to get you back on the road quickly.
              </p>
              <div class="space-y-2 text-sm mb-6" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                <div class="flex justify-between">
                  <span>Level 2 Charging</span>
                  <span style="color: #D4AF37;">$0.25/kWh</span>
                </div>
                <div class="flex justify-between">
                  <span>DC Fast Charging</span>
                  <span style="color: #D4AF37;">$0.35/kWh</span>
                </div>
                <div class="flex justify-between">
                  <span>Membership Discount</span>
                  <span style="color: #D4AF37;">10% Off</span>
                </div>
              </div>
              <button class="w-full py-3 px-6 rounded-lg font-medium transition-all duration-300" style="background-color: #D4AF37; color: #0A0A0A; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#E5C547';" onmouseout="this.style.backgroundColor='#D4AF37';">Start Charging</button>
            </div>
          </div>

          <!-- Oil Change -->
          <div class="rounded-2xl shadow-2xl p-8" style="background-color: #1A1A1A;">
            <div class="text-center">
              <div class="w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-6" style="background-color: rgba(212, 175, 55, 0.1);">
                <svg class="w-10 h-10" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.025a9 9 0 01-5.454 5.454m-9.948-9.948a9 9 0 015.454-5.454m9.948 9.948a9 9 0 01-5.454 5.454m-9.948-9.948a9 9 0 015.454-5.454"></path>
                </svg>
              </div>
              <h3 class="text-2xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Oil Change</h3>
              <p class="mb-6" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
                Quick oil change services to keep your engine running smoothly. 
                Professional service with quality oil and filters.
              </p>
              <div class="space-y-2 text-sm mb-6" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                <div class="flex justify-between">
                  <span>Conventional Oil</span>
                  <span style="color: #D4AF37;">$29.99</span>
                </div>
                <div class="flex justify-between">
                  <span>Synthetic Oil</span>
                  <span style="color: #D4AF37;">$49.99</span>
                </div>
                <div class="flex justify-between">
                  <span>High Mileage</span>
                  <span style="color: #D4AF37;">$39.99</span>
                </div>
              </div>
              <button class="w-full py-3 px-6 rounded-lg font-medium transition-all duration-300" style="background-color: #D4AF37; color: #0A0A0A; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#E5C547';" onmouseout="this.style.backgroundColor='#D4AF37';">Schedule Service</button>
            </div>
          </div>

          <!-- Tire Services -->
          <div class="rounded-2xl shadow-2xl p-8" style="background-color: #1A1A1A;">
            <div class="text-center">
              <div class="w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-6" style="background-color: rgba(212, 175, 55, 0.1);">
                <svg class="w-10 h-10" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9v-9m0-9v9"></path>
                </svg>
              </div>
              <h3 class="text-2xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Tire Services</h3>
              <p class="mb-6" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
                Tire repair, replacement, and maintenance services. 
                Keep your tires in top condition for safe driving.
              </p>
              <div class="space-y-2 text-sm mb-6" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                <div class="flex justify-between">
                  <span>Tire Repair</span>
                  <span style="color: #D4AF37;">$15.00</span>
                </div>
                <div class="flex justify-between">
                  <span>Tire Rotation</span>
                  <span style="color: #D4AF37;">$20.00</span>
                </div>
                <div class="flex justify-between">
                  <span>Tire Installation</span>
                  <span style="color: #D4AF37;">$25.00</span>
                </div>
              </div>
              <button class="w-full py-3 px-6 rounded-lg font-medium transition-all duration-300" style="background-color: #D4AF37; color: #0A0A0A; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#E5C547';" onmouseout="this.style.backgroundColor='#D4AF37';">Get Quote</button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Service Hours & Contact -->
    <section class="py-20" style="background-color: #0F0F0F;">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-4xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Service Hours & Information</h2>
          <div class="w-24 h-1 bg-gradient-to-r from-transparent via-#D4AF37 to-transparent mx-auto mb-6"></div>
          <p class="text-xl" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">
            Most services are available during store hours. Some services like ATM and EV charging are available 24/7.
          </p>
        </div>

        <div class="grid md:grid-cols-2 gap-8">
          <div class="rounded-2xl shadow-2xl p-8" style="background-color: #1A1A1A;">
            <h3 class="text-2xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Service Hours</h3>
            <div class="space-y-3">
              <div class="flex justify-between">
                <span class="font-medium" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Car Wash</span>
                <span style="color: #D4AF37; font-family: 'Inter', sans-serif;">6:00 AM - 10:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span class="font-medium" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Oil Change</span>
                <span style="color: #D4AF37; font-family: 'Inter', sans-serif;">7:00 AM - 7:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span class="font-medium" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Tire Services</span>
                <span style="color: #D4AF37; font-family: 'Inter', sans-serif;">7:00 AM - 7:00 PM</span>
              </div>
              <div class="flex justify-between">
                <span class="font-medium" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">ATM</span>
                <span style="color: #D4AF37; font-family: 'Inter', sans-serif;">24/7</span>
              </div>
              <div class="flex justify-between">
                <span class="font-medium" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">EV Charging</span>
                <span style="color: #D4AF37; font-family: 'Inter', sans-serif;">24/7</span>
              </div>
              <div class="flex justify-between">
                <span class="font-medium" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">Air & Water</span>
                <span style="color: #D4AF37; font-family: 'Inter', sans-serif;">24/7</span>
              </div>
            </div>
          </div>

          <div class="rounded-2xl shadow-2xl p-8" style="background-color: #1A1A1A;">
            <h3 class="text-2xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Contact for Services</h3>
            <div class="space-y-4">
              <div class="flex items-center">
                <svg class="w-5 h-5 mr-3" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
                </svg>
                <a href="tel:+16513952174" class="transition-colors" style="color: #D4AF37; font-family: 'Inter', sans-serif;" onmouseover="this.style.color='#E5C547';" onmouseout="this.style.color='#D4AF37';">(651) 395-2174</a>
              </div>
              <div class="flex items-center">
                <svg class="w-5 h-5 mr-3" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                </svg>
                <a href="mailto:services@goforitgas.com" class="transition-colors" style="color: #D4AF37; font-family: 'Inter', sans-serif;" onmouseover="this.style.color='#E5C547';" onmouseout="this.style.color='#D4AF37';">services@goforitgas.com</a>
              </div>
              <div class="flex items-start">
                <svg class="w-5 h-5 mr-3 mt-1" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                </svg>
                <span style="color: #E5E5E5; font-family: 'Inter', sans-serif;">3255 Viking Blvd NE, East Bethel, MN 55092</span>
              </div>
            </div>
            <div class="mt-6">
              <a href="https://maps.app.goo.gl/H1gsh7KUfgrg6ek49" target="_blank" class="w-full py-3 px-6 rounded-lg font-medium transition-all duration-300 text-center block" style="background-color: #D4AF37; color: #0A0A0A; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#E5C547';" onmouseout="this.style.backgroundColor='#D4AF37';">
                Get Directions
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
useHead({
  title: 'Services - Go For It Liquor',
  meta: [
    { name: 'description', content: 'Additional services at Go For It Liquor including car wash, ATM, EV charging, oil change, tire services, and air & water.' },
    { name: 'keywords', content: 'car wash, ATM, EV charging, oil change, tire services, air water, automotive services, East Bethel, premium spirits' }
  ]
})
</script>
