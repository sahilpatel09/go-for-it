<template>
  <div>
    <!-- Hero Section -->
    <section class="relative h-64 flex items-center justify-center overflow-hidden">
      <div class="absolute inset-0">
        <NuxtImg 
          src="/images/car-wash-hero.jpg" 
          alt="Car wash service at Go For It Gas"
          class="w-full h-full object-cover"
        />
        <div class="hero-overlay"></div>
      </div>
      <div class="relative z-10 text-center text-white">
        <h1 class="heading-2 mb-4 text-shadow-lg">Additional Services</h1>
        <p class="text-lg text-shadow">More than just fuel - we're your complete service stop</p>
      </div>
    </section>

    <!-- Services Grid -->
    <section class="py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="heading-2 mb-4">Our Services</h2>
          <p class="text-xl text-neutral-600 max-w-3xl mx-auto">
            Beyond fuel, we offer a range of services to make your visit convenient and complete. 
            From car care to financial services, we've got you covered.
          </p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Car Wash -->
          <div class="card">
            <div class="card-body text-center">
              <div class="w-20 h-20 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-6">
                <svg class="w-10 h-10 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
                </svg>
              </div>
              <h3 class="heading-3 mb-4">Car Wash</h3>
              <p class="text-neutral-600 mb-6">
                Professional car wash services to keep your vehicle looking its best. 
                Choose from basic wash to premium detailing packages.
              </p>
              <div class="space-y-2 text-sm text-neutral-600 mb-6">
                <div class="flex justify-between">
                  <span>Basic Wash</span>
                  <span>$8.00</span>
                </div>
                <div class="flex justify-between">
                  <span>Premium Wash</span>
                  <span>$12.00</span>
                </div>
                <div class="flex justify-between">
                  <span>Full Detail</span>
                  <span>$25.00</span>
                </div>
              </div>
              <button class="btn-primary w-full">Book Service</button>
            </div>
          </div>

          <!-- ATM -->
          <div class="card">
            <div class="card-body text-center">
              <div class="w-20 h-20 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-6">
                <svg class="w-10 h-10 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"></path>
                </svg>
              </div>
              <h3 class="heading-3 mb-4">ATM Services</h3>
              <p class="text-neutral-600 mb-6">
                24/7 ATM access for your banking needs. Withdraw cash, check balances, 
                and manage your accounts conveniently.
              </p>
              <div class="space-y-2 text-sm text-neutral-600 mb-6">
                <div class="flex justify-between">
                  <span>Cash Withdrawal</span>
                  <span>Available</span>
                </div>
                <div class="flex justify-between">
                  <span>Balance Inquiry</span>
                  <span>Free</span>
                </div>
                <div class="flex justify-between">
                  <span>Deposit</span>
                  <span>Available</span>
                </div>
              </div>
              <button class="btn-primary w-full">Find ATM</button>
            </div>
          </div>

          <!-- Air & Water -->
          <div class="card">
            <div class="card-body text-center">
              <div class="w-20 h-20 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-6">
                <svg class="w-10 h-10 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 10-9.78 2.096A4.001 4.001 0 003 15z"></path>
                </svg>
              </div>
              <h3 class="heading-3 mb-4">Air & Water</h3>
              <p class="text-neutral-600 mb-6">
                Free air for your tires and water for your radiator. 
                Keep your vehicle running smoothly with our complimentary services.
              </p>
              <div class="space-y-2 text-sm text-neutral-600 mb-6">
                <div class="flex justify-between">
                  <span>Tire Air</span>
                  <span>Free</span>
                </div>
                <div class="flex justify-between">
                  <span>Radiator Water</span>
                  <span>Free</span>
                </div>
                <div class="flex justify-between">
                  <span>Windshield Fluid</span>
                  <span>$2.00</span>
                </div>
              </div>
              <button class="btn-primary w-full">Get Service</button>
            </div>
          </div>

          <!-- EV Charging -->
          <div class="card">
            <div class="card-body text-center">
              <div class="w-20 h-20 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-6">
                <svg class="w-10 h-10 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
                </svg>
              </div>
              <h3 class="heading-3 mb-4">EV Charging</h3>
              <p class="text-neutral-600 mb-6">
                Electric vehicle charging stations available for modern drivers. 
                Fast charging options to get you back on the road quickly.
              </p>
              <div class="space-y-2 text-sm text-neutral-600 mb-6">
                <div class="flex justify-between">
                  <span>Level 2 Charging</span>
                  <span>$0.25/kWh</span>
                </div>
                <div class="flex justify-between">
                  <span>DC Fast Charging</span>
                  <span>$0.35/kWh</span>
                </div>
                <div class="flex justify-between">
                  <span>Membership Discount</span>
                  <span>10% Off</span>
                </div>
              </div>
              <button class="btn-primary w-full">Start Charging</button>
            </div>
          </div>

          <!-- Oil Change -->
          <div class="card">
            <div class="card-body text-center">
              <div class="w-20 h-20 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-6">
                <svg class="w-10 h-10 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.025a9 9 0 01-5.454 5.454m-9.948-9.948a9 9 0 015.454-5.454m9.948 9.948a9 9 0 01-5.454 5.454m-9.948-9.948a9 9 0 015.454-5.454"></path>
                </svg>
              </div>
              <h3 class="heading-3 mb-4">Oil Change</h3>
              <p class="text-neutral-600 mb-6">
                Quick oil change services to keep your engine running smoothly. 
                Professional service with quality oil and filters.
              </p>
              <div class="space-y-2 text-sm text-neutral-600 mb-6">
                <div class="flex justify-between">
                  <span>Conventional Oil</span>
                  <span>$29.99</span>
                </div>
                <div class="flex justify-between">
                  <span>Synthetic Oil</span>
                  <span>$49.99</span>
                </div>
                <div class="flex justify-between">
                  <span>High Mileage</span>
                  <span>$39.99</span>
                </div>
              </div>
              <button class="btn-primary w-full">Schedule Service</button>
            </div>
          </div>

          <!-- Tire Services -->
          <div class="card">
            <div class="card-body text-center">
              <div class="w-20 h-20 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-6">
                <svg class="w-10 h-10 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9v-9m0-9v9"></path>
                </svg>
              </div>
              <h3 class="heading-3 mb-4">Tire Services</h3>
              <p class="text-neutral-600 mb-6">
                Tire repair, replacement, and maintenance services. 
                Keep your tires in top condition for safe driving.
              </p>
              <div class="space-y-2 text-sm text-neutral-600 mb-6">
                <div class="flex justify-between">
                  <span>Tire Repair</span>
                  <span>$15.00</span>
                </div>
                <div class="flex justify-between">
                  <span>Tire Rotation</span>
                  <span>$20.00</span>
                </div>
                <div class="flex justify-between">
                  <span>Tire Installation</span>
                  <span>$25.00</span>
                </div>
              </div>
              <button class="btn-primary w-full">Get Quote</button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Service Hours & Contact -->
    <section class="py-16 bg-neutral-50">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="heading-2 mb-4">Service Hours & Information</h2>
          <p class="text-xl text-neutral-600">
            Most services are available during store hours. Some services like ATM and EV charging are available 24/7.
          </p>
        </div>

        <div class="grid md:grid-cols-2 gap-8">
          <div class="card">
            <div class="card-body">
              <h3 class="heading-3 mb-4">Service Hours</h3>
              <div class="space-y-3">
                <div class="flex justify-between">
                  <span class="font-medium">Car Wash</span>
                  <span class="text-neutral-600">6:00 AM - 10:00 PM</span>
                </div>
                <div class="flex justify-between">
                  <span class="font-medium">Oil Change</span>
                  <span class="text-neutral-600">7:00 AM - 7:00 PM</span>
                </div>
                <div class="flex justify-between">
                  <span class="font-medium">Tire Services</span>
                  <span class="text-neutral-600">7:00 AM - 7:00 PM</span>
                </div>
                <div class="flex justify-between">
                  <span class="font-medium">ATM</span>
                  <span class="text-neutral-600">24/7</span>
                </div>
                <div class="flex justify-between">
                  <span class="font-medium">EV Charging</span>
                  <span class="text-neutral-600">24/7</span>
                </div>
                <div class="flex justify-between">
                  <span class="font-medium">Air & Water</span>
                  <span class="text-neutral-600">24/7</span>
                </div>
              </div>
            </div>
          </div>

          <div class="card">
            <div class="card-body">
              <h3 class="heading-3 mb-4">Contact for Services</h3>
              <div class="space-y-4">
                <div class="flex items-center">
                  <svg class="w-5 h-5 text-primary-500 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
                  </svg>
                  <a href="tel:+15551234567" class="hover:text-primary-500 transition-colors">(555) 123-4567</a>
                </div>
                <div class="flex items-center">
                  <svg class="w-5 h-5 text-primary-500 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                  </svg>
                  <a href="mailto:services@goforitgas.com" class="hover:text-primary-500 transition-colors">services@goforitgas.com</a>
                </div>
                <div class="flex items-start">
                  <svg class="w-5 h-5 text-primary-500 mr-3 mt-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                  </svg>
                  <span>123 Main Street, Your City, ST 12345</span>
                </div>
              </div>
              <div class="mt-6">
                <a href="https://maps.google.com/?q=123+Main+Street+Your+City+ST+12345" target="_blank" class="btn-primary w-full">
                  Get Directions
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
useHead({
  title: 'Services - Go For It Gas',
  meta: [
    { name: 'description', content: 'Additional services at Go For It Gas including car wash, ATM, EV charging, oil change, tire services, and air & water.' },
    { name: 'keywords', content: 'car wash, ATM, EV charging, oil change, tire services, air water, automotive services, Your City' }
  ]
})
</script>
