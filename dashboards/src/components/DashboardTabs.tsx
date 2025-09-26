import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { TrendingUp, Users, Home, Info } from "lucide-react"

const dashboards = [
  { 
    id: "economics", 
    title: "Economics", 
    icon: TrendingUp,
    iframeUrl: "https://lookerstudio.google.com/embed/reporting/c25846e6-905a-4f81-b789-b7b2180b195b/page/aHtXF",
    description: "This dashboard provides insights into key economic indicators including GDP growth, inflation rates, unemployment trends, and interest rates. It helps understand the broader economic context that influences housing markets and demographic patterns across different metropolitan areas."
  },
  { 
    id: "demographics", 
    title: "Demographics", 
    icon: Users,
    iframeUrl: "https://lookerstudio.google.com/embed/reporting/cf8c24fc-d7ec-4898-a97b-ce9537ad5f61/page/detXF",
    description: "Explore population demographics, age distributions, migration patterns, and educational attainment across metropolitan areas. This data reveals how demographic shifts impact housing demand, economic growth, and regional development trends."
  },
  { 
    id: "housing", 
    title: "Housing", 
    icon: Home,
    iframeUrl: "https://lookerstudio.google.com/embed/reporting/fe92c6b6-8c46-4a50-b9be-e0e55aba064f/page/aJcXF",
    description: "Analyze housing market trends including home prices, affordability ratios, inventory levels, and construction activity. This dashboard shows how housing costs relate to income levels and population growth, providing insights into market dynamics and accessibility."
  }
]

export function DashboardTabs() {
  return (
    <Tabs defaultValue="economics">
      <div className="flex justify-center mb-8">
        <TabsList className="grid grid-cols-3 bg-white shadow-lg border" style={{ width: '600px' }}>
          {dashboards.map((dashboard) => (
            <TabsTrigger 
              key={dashboard.id} 
              value={dashboard.id} 
              className="flex items-center gap-2 text-sm font-medium px-4 py-3 data-[state=active]:bg-primary data-[state=active]:text-primary-foreground"
            >
              <dashboard.icon className="h-4 w-4" />
              {dashboard.title}
            </TabsTrigger>
          ))}
        </TabsList>
      </div>

      {dashboards.map((dashboard) => (
        <TabsContent key={dashboard.id} value={dashboard.id} className="space-y-6">
          <Card className="max-w-4xl mx-auto shadow-lg border-2">
            <CardHeader className="pb-3">
              <CardTitle className="flex items-center gap-2 text-xl">
                <Info className="h-5 w-5 text-blue-600" />
                About the {dashboard.title} Dashboards
              </CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-muted-foreground leading-relaxed">
                {dashboard.description}
              </p>
            </CardContent>
          </Card>

          {/* Dashboard Container */}
          <div className="max-w-5xl mx-auto">
            <div className="relative" style={{ height: 'calc(100vh - 300px)' }}>
              <iframe
                src={dashboard.iframeUrl}
                width="100%"
                height="100%"
                frameBorder="0"
                className="border-0 rounded-lg"
                allowFullScreen
                sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"
                title={`${dashboard.title} Dashboard`}
              />
            </div>
          </div>
        </TabsContent>
      ))}
    </Tabs>
  )
}