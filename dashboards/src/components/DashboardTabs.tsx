import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs"
import { TrendingUp, Users, Home } from "lucide-react"

const dashboards = [
  { 
    id: "economics", 
    title: "Economics", 
    icon: TrendingUp,
    iframeUrl: "https://lookerstudio.google.com/embed/reporting/c25846e6-905a-4f81-b789-b7b2180b195b/page/aHtXF"
  },
  { 
    id: "demographics", 
    title: "Demographics", 
    icon: Users,
    iframeUrl: "https://lookerstudio.google.com/embed/reporting/cf8c24fc-d7ec-4898-a97b-ce9537ad5f61/page/detXF"
  },
  { 
    id: "housing", 
    title: "Housing", 
    icon: Home,
    iframeUrl: ""
  }
]

export function DashboardTabs() {
  return (
    <Tabs defaultValue="economics">
      <div className="flex justify-center mb-6">
        <TabsList className="grid grid-cols-3" style={{ width: '600px' }}>
          {dashboards.map((dashboard) => (
            <TabsTrigger key={dashboard.id} value={dashboard.id} style={{ fontSize: '18px', padding: '12px 24px' }}>
              {dashboard.title}
            </TabsTrigger>
          ))}
        </TabsList>
      </div>

      {dashboards.map((dashboard) => (
        <TabsContent key={dashboard.id} value={dashboard.id}>
          <div className="w-full h-screen" style={{ marginTop: '20px', marginBottom: '20px' }}>
            <iframe
              src={dashboard.iframeUrl}
              width="100%"
              height="100%"
              frameBorder="0"
              style={{ 
                border: 'none',
                borderRadius: '8px',
                minHeight: '600px'
              }}
              allowFullScreen
              sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"
              title={`${dashboard.title} Dashboard`}
            />
          </div>
        </TabsContent>
      ))}
    </Tabs>
  )
}