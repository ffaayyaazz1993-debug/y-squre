from django.test import TestCase


class GeopoliticsNavigationTests(TestCase):
    def test_homepage_has_geopolitics_dropdown_regions(self):
        response = self.client.get("/")

        self.assertContains(response, "/geopolitics/north-america/")
        self.assertContains(response, "/geopolitics/europe/")
        self.assertContains(response, "/geopolitics/asia/")
        self.assertContains(response, "/geopolitics/asean/")
        self.assertContains(response, "/geopolitics/pacific/")

    def test_region_pages_render(self):
        regions = ["north-america", "europe", "asia", "asean", "pacific"]

        for region in regions:
            with self.subTest(region=region):
                response = self.client.get(f"/geopolitics/{region}/")
                self.assertEqual(response.status_code, 200)

    def test_unknown_region_returns_not_found(self):
        response = self.client.get("/geopolitics/unknown/")

        self.assertEqual(response.status_code, 404)

    def test_north_america_page_has_editorial_coverage_pillars(self):
        response = self.client.get("/geopolitics/north-america/")

        self.assertContains(response, "Trade &amp; Industry")
        self.assertContains(response, "Security &amp; Alliances")
        self.assertContains(response, "Technology &amp; Capital")
        self.assertContains(response, "Policy Signals")

    def test_north_america_sample_article_renders(self):
        response = self.client.get(
            "/geopolitics/north-america/us-canada-relations-markets-crypto/"
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is sample editorial content")
        self.assertContains(response, "US-Canada relations")
