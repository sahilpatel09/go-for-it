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
        <h1 class="heading-2 mb-4 text-shadow-lg text-white">Latest News & Updates</h1>
        <p class="text-lg text-shadow">Stay informed about Go For It Gas and our community</p>
      </div>
    </section>

    <!-- Blog Posts -->
    <section class="py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Featured Post -->
          <div class="md:col-span-2 lg:col-span-1">
            <div class="card h-full">
              <NuxtImg 
                src="/images/blog-featured.jpg" 
                alt="20th Anniversary Celebration"
                class="w-full h-48 object-cover rounded-t-xl"
              />
              <div class="card-body">
                <div class="flex items-center text-sm text-neutral-500 mb-3">
                  <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
                  </svg>
                  <span>December 1, 2024</span>
                </div>
                <h3 class="heading-3 mb-3">Celebrating 20 Years of Service</h3>
                <p class="text-neutral-600 mb-4">
                  Join us as we celebrate two decades of serving our community with quality fuel, 
                  friendly service, and commitment to excellence...
                </p>
                <NuxtLink to="/blog/20th-anniversary" class="text-primary-500 hover:text-primary-600 font-medium">
                  Read More →
                </NuxtLink>
              </div>
            </div>
          </div>

          <!-- Regular Posts -->
          <div class="card">
            <NuxtImg 
              src="/images/blog-ev-charging.jpg" 
              alt="New EV Charging Stations"
              class="w-full h-48 object-cover rounded-t-xl"
            />
            <div class="card-body">
              <div class="flex items-center text-sm text-neutral-500 mb-3">
                <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
                </svg>
                <span>November 28, 2024</span>
              </div>
              <h3 class="heading-4 mb-3">New EV Charging Stations Now Available</h3>
              <p class="text-neutral-600 mb-4">
                We've installed state-of-the-art electric vehicle charging stations to serve 
                the growing number of EV drivers in our community.
              </p>
              <NuxtLink to="/blog/ev-charging-stations" class="text-primary-500 hover:text-primary-600 font-medium">
                Read More →
              </NuxtLink>
            </div>
          </div>

          <div class="card">
            <NuxtImg 
              src="/images/blog-holiday-hours.jpg" 
              alt="Holiday Hours Announcement"
              class="w-full h-48 object-cover rounded-t-xl"
            />
            <div class="card-body">
              <div class="flex items-center text-sm text-neutral-500 mb-3">
                <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
                </svg>
                <span>November 25, 2024</span>
              </div>
              <h3 class="heading-4 mb-3">Holiday Hours and Special Promotions</h3>
              <p class="text-neutral-600 mb-4">
                Check out our special holiday hours and exclusive promotions for the 
                upcoming holiday season.
              </p>
              <NuxtLink to="/blog/holiday-hours" class="text-primary-500 hover:text-primary-600 font-medium">
                Read More →
              </NuxtLink>
            </div>
          </div>

          <div class="card">
            <NuxtImg 
              src="/images/blog-community-support.jpg" 
              alt="Community Support Initiative"
              class="w-full h-48 object-cover rounded-t-xl"
            />
            <div class="card-body">
              <div class="flex items-center text-sm text-neutral-500 mb-3">
                <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
                </svg>
                <span>November 20, 2024</span>
              </div>
              <h3 class="heading-4 mb-3">Supporting Local Schools</h3>
              <p class="text-neutral-600 mb-4">
                Learn about our ongoing commitment to supporting local schools and 
                educational programs in our community.
              </p>
              <NuxtLink to="/blog/supporting-schools" class="text-primary-500 hover:text-primary-600 font-medium">
                Read More →
              </NuxtLink>
            </div>
          </div>

          <div class="card">
            <NuxtImg 
              src="/images/blog-fuel-tips.jpg" 
              alt="Fuel Efficiency Tips"
              class="w-full h-48 object-cover rounded-t-xl"
            />
            <div class="card-body">
              <div class="flex items-center text-sm text-neutral-500 mb-3">
                <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
                </svg>
                <span>November 15, 2024</span>
              </div>
              <h3 class="heading-4 mb-3">Tips for Better Fuel Efficiency</h3>
              <p class="text-neutral-600 mb-4">
                Discover simple ways to improve your vehicle's fuel efficiency and 
                save money at the pump.
              </p>
              <NuxtLink to="/blog/fuel-efficiency-tips" class="text-primary-500 hover:text-primary-600 font-medium">
                Read More →
              </NuxtLink>
            </div>
          </div>

          <div class="card">
            <NuxtImg 
              src="/images/blog-new-services.jpg" 
              alt="New Services Available"
              class="w-full h-48 object-cover rounded-t-xl"
            />
            <div class="card-body">
              <div class="flex items-center text-sm text-neutral-500 mb-3">
                <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
                </svg>
                <span>November 10, 2024</span>
              </div>
              <h3 class="heading-4 mb-3">New Services Now Available</h3>
              <p class="text-neutral-600 mb-4">
                We've expanded our services to include oil changes, tire repair, 
                and enhanced car wash options.
              </p>
              <NuxtLink to="/blog/new-services" class="text-primary-500 hover:text-primary-600 font-medium">
                Read More →
              </NuxtLink>
            </div>
          </div>
        </div>

        <!-- Load More Button -->
        <div class="text-center mt-12">
          <button class="btn-outline">
            Load More Posts
          </button>
        </div>
      </div>
    </section>

    <!-- Newsletter Signup -->
    <section class="py-16 bg-primary-500">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center text-white">
        <h2 class="heading-2 mb-4">Stay Updated</h2>
        <p class="text-xl mb-8">
          Subscribe to our newsletter for the latest news, promotions, and community updates.
        </p>
        
        <form @submit.prevent="subscribeNewsletter" class="max-w-md mx-auto">
          <div class="flex flex-col sm:flex-row gap-4">
            <input 
              type="email" 
              v-model="newsletterEmail"
              required
              placeholder="Enter your email address"
              class="flex-1 px-4 py-3 rounded-lg text-neutral-900 focus:outline-none focus:ring-2 focus:ring-white"
            >
            <button 
              type="submit" 
              :disabled="isSubscribing"
              class="btn-secondary"
            >
              <span v-if="isSubscribing" class="loading-dots">
                <div></div>
                <div></div>
                <div></div>
              </span>
              <span v-else>Subscribe</span>
            </button>
          </div>
        </form>
        
        <p class="text-sm text-primary-100 mt-4">
          We respect your privacy. Unsubscribe at any time.
        </p>
      </div>
    </section>
  </div>
</template>

<script setup>
const newsletterEmail = ref('')
const isSubscribing = ref(false)

const subscribeNewsletter = async () => {
  isSubscribing.value = true
  
  try {
    // Simulate newsletter subscription
    await new Promise(resolve => setTimeout(resolve, 2000))
    
    newsletterEmail.value = ''
    alert('Thank you for subscribing to our newsletter!')
    
  } catch (error) {
    console.error('Newsletter subscription error:', error)
    alert('There was an error subscribing. Please try again.')
  } finally {
    isSubscribing.value = false
  }
}

useHead({
  title: 'Blog - Go For It Gas',
  meta: [
    { name: 'description', content: 'Latest news and updates from Go For It Gas. Stay informed about promotions, new services, community events, and more.' },
    { name: 'keywords', content: 'news, updates, blog, promotions, community events, new services, East Bethel' }
  ]
})
</script>
