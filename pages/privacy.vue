<template>
  <div>
    <!-- Hero Section -->
    <section class="relative h-48 flex items-center justify-center overflow-hidden">
      <div class="absolute inset-0">
        <NuxtImg 
          src="/images/privacy-hero.jpg" 
          alt="Privacy Policy"
          class="w-full h-full object-cover"
        />
        <div class="hero-overlay"></div>
      </div>
      <div class="relative z-10 text-center text-white">
        <h1 class="heading-2 mb-4 text-shadow-lg">Privacy Policy</h1>
        <p class="text-lg text-shadow">How we protect your personal information</p>
      </div>
    </section>

    <!-- Privacy Policy Content -->
    <section class="py-16">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="prose prose-lg max-w-none">
          <div class="bg-white rounded-xl shadow-soft p-8 mb-8">
            <p class="text-sm text-neutral-500 mb-6">Last updated: December 1, 2024</p>
            
            <h2 class="heading-2 mb-6">Introduction</h2>
            <p class="text-neutral-700 mb-6">
              Go For It Gas ("we," "our," or "us") is committed to protecting your privacy. This Privacy Policy 
              explains how we collect, use, disclose, and safeguard your information when you visit our website 
              or use our services.
            </p>

            <h3 class="heading-3 mb-4">Information We Collect</h3>
            <div class="mb-6">
              <h4 class="heading-4 mb-3">Personal Information</h4>
              <p class="text-neutral-700 mb-4">We may collect personal information that you voluntarily provide to us, including:</p>
              <ul class="text-neutral-700 space-y-2 mb-4">
                <li>• Name and contact information (email, phone number, address)</li>
                <li>• Payment information for transactions</li>
                <li>• Loyalty program information</li>
                <li>• Feedback and communications with us</li>
                <li>• Job application information</li>
              </ul>
            </div>

            <div class="mb-6">
              <h4 class="heading-4 mb-3">Automatically Collected Information</h4>
              <p class="text-neutral-700 mb-4">We may automatically collect certain information about your device and usage, including:</p>
              <ul class="text-neutral-700 space-y-2 mb-4">
                <li>• IP address and device information</li>
                <li>• Browser type and version</li>
                <li>• Pages visited and time spent on our website</li>
                <li>• Referring website information</li>
                <li>• Location data (with your permission)</li>
              </ul>
            </div>

            <h3 class="heading-3 mb-4">How We Use Your Information</h3>
            <p class="text-neutral-700 mb-4">We use the information we collect for various purposes, including:</p>
            <ul class="text-neutral-700 space-y-2 mb-6">
              <li>• Providing and improving our services</li>
              <li>• Processing transactions and payments</li>
              <li>• Communicating with you about promotions and updates</li>
              <li>• Responding to your inquiries and feedback</li>
              <li>• Managing our loyalty program</li>
              <li>• Analyzing website usage and trends</li>
              <li>• Complying with legal obligations</li>
            </ul>

            <h3 class="heading-3 mb-4">Information Sharing</h3>
            <p class="text-neutral-700 mb-4">We do not sell, trade, or otherwise transfer your personal information to third parties except:</p>
            <ul class="text-neutral-700 space-y-2 mb-6">
              <li>• With your explicit consent</li>
              <li>• To trusted service providers who assist us in operating our business</li>
              <li>• When required by law or to protect our rights</li>
              <li>• In connection with a business transfer or acquisition</li>
            </ul>

            <h3 class="heading-3 mb-4">Data Security</h3>
            <p class="text-neutral-700 mb-6">
              We implement appropriate security measures to protect your personal information against unauthorized 
              access, alteration, disclosure, or destruction. However, no method of transmission over the internet 
              or electronic storage is 100% secure.
            </p>

            <h3 class="heading-3 mb-4">Your Rights</h3>
            <p class="text-neutral-700 mb-4">You have the right to:</p>
            <ul class="text-neutral-700 space-y-2 mb-6">
              <li>• Access and update your personal information</li>
              <li>• Request deletion of your personal information</li>
              <li>• Opt out of marketing communications</li>
              <li>• Request a copy of your data</li>
              <li>• Withdraw consent for data processing</li>
            </ul>

            <h3 class="heading-3 mb-4">Cookies and Tracking</h3>
            <p class="text-neutral-700 mb-6">
              We use cookies and similar tracking technologies to enhance your experience on our website. 
              You can control cookie settings through your browser preferences.
            </p>

            <h3 class="heading-3 mb-4">Third-Party Links</h3>
            <p class="text-neutral-700 mb-6">
              Our website may contain links to third-party websites. We are not responsible for the privacy 
              practices or content of these external sites.
            </p>

            <h3 class="heading-3 mb-4">Children's Privacy</h3>
            <p class="text-neutral-700 mb-6">
              Our services are not directed to children under 13. We do not knowingly collect personal 
              information from children under 13.
            </p>

            <h3 class="heading-3 mb-4">Changes to This Policy</h3>
            <p class="text-neutral-700 mb-6">
              We may update this Privacy Policy from time to time. We will notify you of any changes by 
              posting the new Privacy Policy on this page and updating the "Last updated" date.
            </p>

            <h3 class="heading-3 mb-4">Contact Us</h3>
            <p class="text-neutral-700 mb-4">If you have any questions about this Privacy Policy, please contact us:</p>
            <div class="bg-neutral-50 rounded-lg p-6">
              <div class="space-y-2">
                <p><strong>Go For It Gas</strong></p>
                <p>3255 Viking Blvd NE<br>East Bethel, MN 55092</p>
                <p>Phone: <a href="tel:+16513952174" class="text-primary-500 hover:text-primary-600">(651) 395-2174</a></p>
                <p>Email: <a href="mailto:privacy@goforitgas.com" class="text-primary-500 hover:text-primary-600">privacy@goforitgas.com</a></p>
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
  title: 'Privacy Policy — Go For It Liquor East Bethel, MN | Data Protection',
  meta: [
    { name: 'description', content: 'Privacy Policy for Go For It Liquor in East Bethel, MN. Learn how we collect, use, and protect your personal information.' },
    { name: 'keywords', content: 'privacy policy, Go For It Liquor, East Bethel MN, data protection, personal information' },
    { name: 'canonical', content: 'https://go-for-it-wheat.vercel.app/privacy' },
    { name: 'robots', content: 'noindex, nofollow' }
  ],
  link: [
    { rel: 'sitemap', href: '/sitemap.xml', type: 'application/xml' }
  ]
})
</script>
