{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8e00346b",
   "metadata": {},
   "source": [
    "# PART 1: DATA LOADING & PREPROCESSING\n",
    "## Setup, Data Loading, and Calculated Fields\n",
    "\n",
    "This section handles all data operations, imports, and derived field calculations needed for the analysis."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "42d533d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "📊 Imports and aesthetic configuration completed!\n"
     ]
    }
   ],
   "source": [
    "# === IMPORTS & SETUP ===\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import plotly.express as px\n",
    "import plotly.graph_objects as go\n",
    "from plotly.subplots import make_subplots\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')\n",
    "\n",
    "# === AESTHETIC CONFIGURATION ===\n",
    "# FUTURISTIC GLOWING COLOR SCHEME (matching dashboard)\n",
    "COLORS = {\n",
    "    'primary': '#8B5FBF',      # Purple gradient\n",
    "    'secondary': '#22D3EE',    # Cyan blue  \n",
    "    'accent': '#F97316',       # Orange accent\n",
    "    'success': '#10B981',      # Green\n",
    "    'warning': '#F59E0B',      # Amber\n",
    "    'danger': '#EF4444',       # Red\n",
    "    'pink': '#EC4899',         # Pink for cards\n",
    "    'dark_bg': '#0A0A1A',      # Ultra dark background\n",
    "    'card_bg': '#1A1A2E',      # Dark card background with glow\n",
    "    'sidebar_bg': '#16213E',   # Glowing sidebar\n",
    "    'light': '#FFFFFF',        # White\n",
    "    'text': '#E2E8F0',         # Light gray text\n",
    "    'text_dim': '#94A3B8',     # Dimmed text\n",
    "    'neon_blue': '#00F5FF',    # Neon blue glow\n",
    "    'neon_purple': '#BF40BF',  # Neon purple glow\n",
    "    'neon_green': '#39FF14',   # Neon green glow\n",
    "    'glow_shadow': 'rgba(34, 211, 238, 0.4)',  # Glowing shadow\n",
    "    'neutral': '#6C7B7F'       # Cool gray\n",
    "}\n",
    "\n",
    "# Professional color palettes using dashboard colors\n",
    "citizenship_colors = [COLORS['primary'], COLORS['secondary'], COLORS['accent'], COLORS['pink']]\n",
    "funding_colors = [COLORS['neon_blue'], COLORS['neon_purple'], COLORS['neon_green'], COLORS['accent'], COLORS['pink']]\n",
    "gender_colors = [COLORS['primary'], COLORS['secondary']]\n",
    "\n",
    "# Global styling with futuristic dark theme\n",
    "template_config = {\n",
    "    'layout': {\n",
    "        'font': {'family': 'Orbitron, monospace', 'size': 12, 'color': COLORS['light']},\n",
    "        'paper_bgcolor': COLORS['dark_bg'],\n",
    "        'plot_bgcolor': 'rgba(0,0,0,0)',\n",
    "        'margin': {'l': 80, 'r': 120, 't': 150, 'b': 80},\n",
    "        'hovermode': 'closest',\n",
    "        'showlegend': True,\n",
    "        'legend': {\n",
    "            'orientation': 'h',\n",
    "            'yanchor': 'bottom',\n",
    "            'y': -0.2,\n",
    "            'xanchor': 'center',\n",
    "            'x': 0.5,\n",
    "            'bgcolor': 'rgba(255,255,255,0.8)',\n",
    "            'bordercolor': COLORS['neutral'],\n",
    "            'borderwidth': 1\n",
    "        }\n",
    "    }\n",
    "}\n",
    "\n",
    "print(\"📊 Imports and aesthetic configuration completed!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b3301ca7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "📊 Loading and preprocessing data...\n",
      "✅ Data loaded successfully\n",
      "✅ Data loading completed!\n"
     ]
    }
   ],
   "source": [
    "# === DATA LOADING & PREPROCESSING ===\n",
    "print(\"📊 Loading and preprocessing data...\")\n",
    "\n",
    "# Load datasets\n",
    "try:\n",
    "    profiles = pd.read_excel(\"Cleaned_Student_Profiles.xlsx\")\n",
    "    results = pd.read_excel(\"Cleaned_Semester_Results.xlsx\")\n",
    "    courses = pd.read_excel(\"Cleaned_Course_Codes.xlsx\")\n",
    "    print(\"✅ Data loaded successfully\")\n",
    "except FileNotFoundError as e:\n",
    "    print(f\"❌ Error loading data: {e}\")\n",
    "    # Create mock data for demonstration\n",
    "    print(\"🔄 Creating mock data for demonstration...\")\n",
    "    np.random.seed(42)\n",
    "    n_students = 500\n",
    "    \n",
    "    profiles = pd.DataFrame({\n",
    "        'STUDENT ID': [f'STU{i:05d}' for i in range(1, n_students + 1)],\n",
    "        'GENDER': np.random.choice(['Male', 'Female'], n_students),\n",
    "        'CITIZENSHIP': np.random.choice(['Citizen', 'PR', 'International'], n_students, p=[0.6, 0.25, 0.15]),\n",
    "        'HIGHEST QUALIFICATION': np.random.choice(['Diploma', 'Bachelor', 'Master', 'PhD'], n_students, p=[0.3, 0.4, 0.25, 0.05]),\n",
    "        'COURSE FUNDING': np.random.choice(['Self-Funded', 'Scholarship', 'Sponsored', 'Loan'], n_students),\n",
    "        'COMMENCEMENT DATE': pd.date_range('2020-01-01', '2023-12-31', periods=n_students),\n",
    "        'COMPLETION DATE': pd.date_range('2022-01-01', '2026-12-31', periods=n_students),\n",
    "        'FULL-TIME OR PART-TIME': np.random.choice(['Full-Time', 'Part-Time'], n_students, p=[0.7, 0.3])\n",
    "    })\n",
    "    \n",
    "    # Generate results data\n",
    "    periods = ['2020 Sem 1', '2020 Sem 2', '2021 Sem 1', '2021 Sem 2', '2022 Sem 1', '2022 Sem 2', '2023 Sem 1', '2023 Sem 2']\n",
    "    n_results = n_students * 3  # Average 3 semesters per student\n",
    "    results = pd.DataFrame({\n",
    "        'STUDENT ID': np.random.choice(profiles['STUDENT ID'], n_results),\n",
    "        'PERIOD': np.random.choice(periods, n_results),\n",
    "        'GPA': np.random.beta(2, 1, n_results) * 3 + 1  # GPA between 1-4\n",
    "    })\n",
    "    results['GPA'] = results['GPA'].round(2)\n",
    "\n",
    "# Parse dates\n",
    "date_columns = ['COMMENCEMENT DATE', 'COMPLETION DATE']\n",
    "for col in date_columns:\n",
    "    if col in profiles.columns:\n",
    "        profiles[col] = pd.to_datetime(profiles[col], errors='coerce')\n",
    "\n",
    "print(\"✅ Data loading completed!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e9ab78d8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "🔧 Calculating derived metrics...\n",
      "🔧 Creating advanced calculated fields...\n",
      "📈 Dataset Summary: 285 students, 531 semester records\n",
      "✅ All calculated fields completed!\n",
      "============================================================\n"
     ]
    }
   ],
   "source": [
    "# === CALCULATE DERIVED METRICS ===\n",
    "print(\"🔧 Calculating derived metrics...\")\n",
    "\n",
    "# 1. Cumulative GPA per student\n",
    "cum_gpa = results.groupby('STUDENT ID', as_index=False)['GPA'].agg({\n",
    "    'CUMULATIVE_GPA': 'mean',\n",
    "    'TOTAL_SEMESTERS': 'count',\n",
    "    'BEST_GPA': 'max',\n",
    "    'WORST_GPA': 'min'\n",
    "}).round(2)\n",
    "\n",
    "# 2. Merge with profiles\n",
    "df = profiles.merge(cum_gpa, on='STUDENT ID', how='left')\n",
    "\n",
    "# 3. Calculate completion time and academic outcome\n",
    "df['COMPLETION_MONTHS'] = (df['COMPLETION DATE'] - df['COMMENCEMENT DATE']).dt.days / 30.44\n",
    "df['ACADEMIC_OUTCOME'] = np.where(df['CUMULATIVE_GPA'] >= 2.0, 'Pass', 'Fail')\n",
    "df['PERFORMANCE_TIER'] = pd.cut(df['CUMULATIVE_GPA'], \n",
    "                               bins=[0, 2.0, 2.5, 3.0, 4.0], \n",
    "                               labels=['Poor', 'Average', 'Good', 'Excellent'])\n",
    "\n",
    "# 4. NEW CALCULATED FIELDS - Advanced Analytics\n",
    "print(\"🔧 Creating advanced calculated fields...\")\n",
    "\n",
    "# Academic Progress Metrics\n",
    "df['GPA_IMPROVEMENT'] = df['BEST_GPA'] - df['WORST_GPA']  # Range of performance\n",
    "df['GPA_VOLATILITY'] = df['GPA_IMPROVEMENT'] / df['TOTAL_SEMESTERS']  # Volatility per semester\n",
    "df['ACADEMIC_EFFICIENCY'] = df['CUMULATIVE_GPA'] / df['COMPLETION_MONTHS']  # Performance per month\n",
    "df['STUDY_INTENSITY'] = df['TOTAL_SEMESTERS'] / df['COMPLETION_MONTHS'] * 12  # Semesters per year\n",
    "\n",
    "# Performance Categories\n",
    "df['FAST_TRACK'] = np.where(df['COMPLETION_MONTHS'] <= 24, 'Fast Track', \n",
    "                   np.where(df['COMPLETION_MONTHS'] <= 36, 'Standard', 'Extended'))\n",
    "\n",
    "# Financial & Demographic Scoring\n",
    "funding_priority = {'Scholarship': 4, 'Sponsored': 3, 'Loan': 2, 'Self-Funded': 1}\n",
    "df['FUNDING_PRIORITY'] = df['COURSE FUNDING'].map(funding_priority)\n",
    "\n",
    "# Academic Risk Assessment\n",
    "df['RISK_SCORE'] = (\n",
    "    np.where(df['CUMULATIVE_GPA'] < 2.0, 3, 0) +  # Academic risk\n",
    "    np.where(df['COMPLETION_MONTHS'] > 48, 2, 0) +  # Time risk\n",
    "    np.where(df['GPA_VOLATILITY'] > 0.1, 1, 0)     # Consistency risk\n",
    ")\n",
    "df['RISK_CATEGORY'] = pd.cut(df['RISK_SCORE'], \n",
    "                            bins=[-1, 0, 2, 6], \n",
    "                            labels=['Low Risk', 'Medium Risk', 'High Risk'])\n",
    "\n",
    "# Success Prediction Score (0-100)\n",
    "df['SUCCESS_SCORE'] = (\n",
    "    (df['CUMULATIVE_GPA'] / 4.0 * 40) +  # 40% weight on GPA\n",
    "    (np.where(df['COMPLETION_MONTHS'] <= 36, 30, \n",
    "             np.where(df['COMPLETION_MONTHS'] <= 48, 20, 10))) +  # 30% on completion speed\n",
    "    (df['FUNDING_PRIORITY'] * 5) +  # 20% on funding\n",
    "    (np.where(df['GPA_VOLATILITY'] <= 0.05, 10, \n",
    "             np.where(df['GPA_VOLATILITY'] <= 0.1, 5, 0)))  # 10% on consistency\n",
    ").round(1)\n",
    "\n",
    "# 5. Prepare period-wise data for time series analysis\n",
    "period_data = results.merge(profiles[['STUDENT ID', 'CITIZENSHIP', 'GENDER', 'COURSE FUNDING']], on='STUDENT ID')\n",
    "period_summary = period_data.groupby(['PERIOD', 'CITIZENSHIP'], as_index=False)['GPA'].mean().round(2)\n",
    "\n",
    "print(f\"📈 Dataset Summary: {len(df)} students, {len(results)} semester records\")\n",
    "print(\"✅ All calculated fields completed!\")\n",
    "print(\"=\" * 60)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a3342861",
   "metadata": {},
   "source": [
    "# PART 2: INDIVIDUAL CHART CREATIONS\n",
    "## Professional Analytics Charts with Template Aesthetics\n",
    "\n",
    "This section creates 4 individual charts with modern styling, interactive elements, and comprehensive insights matching the dashboard template aesthetic."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8e40d264",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "🎨 Creating Chart 1: Student Distribution Treemap...\n"
     ]
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "branchvalues": "total",
         "customdata": [
          [
           9.1,
           26
          ],
          [
           30.2,
           86
          ],
          [
           5.6,
           16
          ],
          [
           8.4,
           24
          ],
          [
           0.4,
           1
          ],
          [
           0.4,
           1
          ],
          [
           19.6,
           56
          ],
          [
           1.1,
           3
          ],
          [
           2.1,
           6
          ],
          [
           1.4,
           4
          ],
          [
           1.4,
           4
          ],
          [
           0.4,
           1
          ],
          [
           2.5,
           7
          ],
          [
           13,
           37
          ],
          [
           3.5,
           10
          ],
          [
           1.1,
           3
          ],
          [
           "(?)",
           21.352941176470587
          ],
          [
           "(?)",
           63.81283422459893
          ],
          [
           "(?)",
           12.586206896551724
          ],
          [
           "(?)",
           18.294117647058822
          ],
          [
           0.4,
           1
          ],
          [
           "(?)",
           21.352941176470587
          ],
          [
           "(?)",
           56.80995475113122
          ],
          [
           "(?)",
           12.2
          ]
         ],
         "domain": {
          "x": [
           0,
           1
          ],
          "y": [
           0,
           1
          ]
         },
         "hovertemplate": "<b>%{label}</b><br>Count: %{value}<br>Percentage: %{customdata[0]:.1f}%<extra></extra>",
         "ids": [
          "FOREIGNER/F/Individual",
          "SG CITIZEN/F/Individual",
          "SG PR/F/Individual",
          "SG CITIZEN/M/Individual",
          "SG PR/M/Individual",
          "FOREIGNER/F/Individual - SFC",
          "SG CITIZEN/F/Individual - SFC",
          "SG PR/F/Individual - SFC",
          "SG CITIZEN/M/Individual - SFC",
          "SG CITIZEN/F/Individual - SFC + $1000 SCHOLARSHIP",
          "SG CITIZEN/F/Individual - Waived App Fee",
          "SG CITIZEN/M/Individual - Waived App Fee",
          "FOREIGNER/F/Sponsored",
          "SG CITIZEN/F/Sponsored",
          "SG PR/F/Sponsored",
          "SG CITIZEN/M/Sponsored",
          "FOREIGNER/F",
          "SG CITIZEN/F",
          "SG PR/F",
          "SG CITIZEN/M",
          "SG PR/M",
          "FOREIGNER",
          "SG CITIZEN",
          "SG PR"
         ],
         "labels": [
          "Individual",
          "Individual",
          "Individual",
          "Individual",
          "Individual",
          "Individual - SFC",
          "Individual - SFC",
          "Individual - SFC",
          "Individual - SFC",
          "Individual - SFC + $1000 SCHOLARSHIP",
          "Individual - Waived App Fee",
          "Individual - Waived App Fee",
          "Sponsored",
          "Sponsored",
          "Sponsored",
          "Sponsored",
          "F",
          "F",
          "F",
          "M",
          "M",
          "FOREIGNER",
          "SG CITIZEN",
          "SG PR"
         ],
         "marker": {
          "coloraxis": "coloraxis",
          "colors": [
           26,
           86,
           16,
           24,
           1,
           1,
           56,
           3,
           6,
           4,
           4,
           1,
           7,
           37,
           10,
           3,
           21.352941176470587,
           63.81283422459893,
           12.586206896551724,
           18.294117647058822,
           1,
           21.352941176470587,
           56.80995475113122,
           12.2
          ]
         },
         "name": "",
         "parents": [
          "FOREIGNER/F",
          "SG CITIZEN/F",
          "SG PR/F",
          "SG CITIZEN/M",
          "SG PR/M",
          "FOREIGNER/F",
          "SG CITIZEN/F",
          "SG PR/F",
          "SG CITIZEN/M",
          "SG CITIZEN/F",
          "SG CITIZEN/F",
          "SG CITIZEN/M",
          "FOREIGNER/F",
          "SG CITIZEN/F",
          "SG PR/F",
          "SG CITIZEN/M",
          "FOREIGNER",
          "SG CITIZEN",
          "SG PR",
          "SG CITIZEN",
          "SG PR",
          "",
          "",
          ""
         ],
         "textfont": {
          "color": "#FFFFFF",
          "size": 11
         },
         "textinfo": "label+value+percent parent",
         "type": "treemap",
         "values": [
          26,
          86,
          16,
          24,
          1,
          1,
          56,
          3,
          6,
          4,
          4,
          1,
          7,
          37,
          10,
          3,
          34,
          187,
          29,
          34,
          1,
          34,
          221,
          30
         ]
        }
       ],
       "layout": {
        "coloraxis": {
         "colorbar": {
          "title": {
           "text": "COUNT"
          }
         },
         "colorscale": [
          [
           0,
           "#440154"
          ],
          [
           0.1111111111111111,
           "#482878"
          ],
          [
           0.2222222222222222,
           "#3e4989"
          ],
          [
           0.3333333333333333,
           "#31688e"
          ],
          [
           0.4444444444444444,
           "#26828e"
          ],
          [
           0.5555555555555556,
           "#1f9e89"
          ],
          [
           0.6666666666666666,
           "#35b779"
          ],
          [
           0.7777777777777778,
           "#6ece58"
          ],
          [
           0.8888888888888888,
           "#b5de2b"
          ],
          [
           1,
           "#fde725"
          ]
         ]
        },
        "font": {
         "color": "#FFFFFF",
         "family": "Orbitron, monospace",
         "size": 12
        },
        "height": 700,
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "b": 20,
         "l": 20,
         "r": 20,
         "t": 150
        },
        "paper_bgcolor": "#0A0A1A",
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "font": {
          "color": "#FFFFFF",
          "size": 18
         },
         "text": "<b>🌍 Student Population Breakdown</b><br><sub>Distribution by Citizenship, Gender, and Funding Type • Click to drill down</sub>",
         "x": 0.5
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Chart 1 completed!\n"
     ]
    }
   ],
   "source": [
    "# === CHART 1: PLOTLY EXPRESS - Student Distribution Treemap ===\n",
    "print(\"🎨 Creating Chart 1: Student Distribution Treemap...\")\n",
    "\n",
    "# Prepare hierarchical data for treemap\n",
    "treemap_data = df.groupby(['CITIZENSHIP', 'GENDER', 'COURSE FUNDING']).size().reset_index(name='COUNT')\n",
    "treemap_data['PERCENTAGE'] = (treemap_data['COUNT'] / len(df) * 100).round(1)\n",
    "\n",
    "fig1 = px.treemap(\n",
    "    treemap_data,\n",
    "    path=['CITIZENSHIP', 'GENDER', 'COURSE FUNDING'],\n",
    "    values='COUNT',\n",
    "    title='<b>🌍 Student Population Breakdown</b><br><sub>Distribution by Citizenship, Gender, and Funding Type • Click to drill down</sub>',\n",
    "    color='COUNT',\n",
    "    color_continuous_scale='Viridis',\n",
    "    hover_data={'PERCENTAGE': ':.1f%'}\n",
    ")\n",
    "\n",
    "fig1.update_layout(\n",
    "    font=dict(family='Orbitron, monospace', size=12, color=COLORS['light']),\n",
    "    title_font_size=18,\n",
    "    title_x=0.5,\n",
    "    title_font_color=COLORS['light'],\n",
    "    paper_bgcolor=COLORS['dark_bg'],\n",
    "    height=700,\n",
    "    margin=dict(t=150, l=20, r=20, b=20)\n",
    ")\n",
    "\n",
    "fig1.update_traces(\n",
    "    textinfo='label+value+percent parent',\n",
    "    textfont_size=11,\n",
    "    textfont_color=COLORS['light'],\n",
    "    hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{customdata[0]:.1f}%<extra></extra>'\n",
    ")\n",
    "\n",
    "fig1.show()\n",
    "print(\"✅ Chart 1 completed!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "017d2e00",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "🎨 Creating Chart 2: Interactive GPA vs Completion Time Analysis...\n"
     ]
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "%{text}<extra></extra>",
         "marker": {
          "color": [
           79,
           66,
           74,
           71,
           89,
           82,
           81,
           79,
           71,
           66,
           74,
           89,
           88,
           67,
           81,
           79,
           65,
           92,
           83,
           94,
           83,
           89,
           87,
           82,
           93,
           90,
           81,
           87,
           90,
           87,
           87,
           92,
           91,
           84,
           83,
           85,
           90,
           85,
           87
          ],
          "colorbar": {
           "len": 0.8,
           "tickfont": {
            "size": 10
           },
           "title": {
            "font": {
             "family": "Arial Black",
             "size": 12
            },
            "text": "Success<br>Score<br>(0-100)"
           }
          },
          "colorscale": [
           [
            0,
            "#440154"
           ],
           [
            0.1111111111111111,
            "#482878"
           ],
           [
            0.2222222222222222,
            "#3e4989"
           ],
           [
            0.3333333333333333,
            "#31688e"
           ],
           [
            0.4444444444444444,
            "#26828e"
           ],
           [
            0.5555555555555556,
            "#1f9e89"
           ],
           [
            0.6666666666666666,
            "#35b779"
           ],
           [
            0.7777777777777778,
            "#6ece58"
           ],
           [
            0.8888888888888888,
            "#b5de2b"
           ],
           [
            1,
            "#fde725"
           ]
          ],
          "line": {
           "color": "white",
           "width": 2
          },
          "opacity": 0.8,
          "showscale": true,
          "size": [
           12,
           16,
           16,
           12,
           12,
           16,
           16,
           16,
           16,
           16,
           16,
           12,
           12,
           16,
           16,
           16,
           16,
           12,
           12,
           12,
           12,
           12,
           12,
           12,
           12,
           12,
           12,
           12,
           12,
           12,
           12,
           12,
           12,
           12,
           12,
           12,
           12,
           12,
           12
          ],
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "SG CITIZEN (39 students)",
         "text": [
          "Student ID: 1101-009/005<br>GPA: 2.90<br>Completion: 17.0 months<br>Success Score: 79.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 1101-009/007<br>GPA: 2.10<br>Completion: 17.0 months<br>Success Score: 66.0<br>Risk Category: Medium Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 1101-009/009<br>GPA: 2.90<br>Completion: 17.0 months<br>Success Score: 74.0<br>Risk Category: Medium Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 1101-010/002<br>GPA: 2.10<br>Completion: 17.0 months<br>Success Score: 71.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 1101-010/004<br>GPA: 3.90<br>Completion: 17.0 months<br>Success Score: 89.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 1101-010/011<br>GPA: 3.70<br>Completion: 17.0 months<br>Success Score: 82.0<br>Risk Category: Medium Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 1101-012/010<br>GPA: 3.60<br>Completion: 17.0 months<br>Success Score: 81.0<br>Risk Category: Medium Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 1101-012/011<br>GPA: 3.40<br>Completion: 17.0 months<br>Success Score: 79.0<br>Risk Category: Medium Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 1102-001/002<br>GPA: 2.60<br>Completion: 17.0 months<br>Success Score: 71.0<br>Risk Category: Medium Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 1102-001/005<br>GPA: 2.10<br>Completion: 17.0 months<br>Success Score: 66.0<br>Risk Category: Medium Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 1102-001/007<br>GPA: 2.90<br>Completion: 17.0 months<br>Success Score: 74.0<br>Risk Category: Medium Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 1102-002/002<br>GPA: 3.90<br>Completion: 17.0 months<br>Success Score: 89.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 1102-004/001<br>GPA: 3.80<br>Completion: 17.0 months<br>Success Score: 88.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 1102-004/003<br>GPA: 2.20<br>Completion: 17.0 months<br>Success Score: 67.0<br>Risk Category: Medium Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 1102-004/004<br>GPA: 3.60<br>Completion: 17.0 months<br>Success Score: 81.0<br>Risk Category: Medium Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 1102-004/005<br>GPA: 3.40<br>Completion: 17.0 months<br>Success Score: 79.0<br>Risk Category: Medium Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 1102-004/008<br>GPA: 2.00<br>Completion: 17.0 months<br>Success Score: 65.0<br>Risk Category: Medium Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2101-107/003<br>GPA: 3.70<br>Completion: 5.0 months<br>Success Score: 92.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2101-107/006<br>GPA: 2.80<br>Completion: 5.0 months<br>Success Score: 83.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2101-108A/004<br>GPA: 3.90<br>Completion: 2.3 months<br>Success Score: 94.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2101-109/002<br>GPA: 2.80<br>Completion: 4.5 months<br>Success Score: 83.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2101-109/007<br>GPA: 3.40<br>Completion: 4.5 months<br>Success Score: 89.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2101-110/001<br>GPA: 3.20<br>Completion: 5.0 months<br>Success Score: 87.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-063/006<br>GPA: 2.70<br>Completion: 4.9 months<br>Success Score: 82.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-064/002<br>GPA: 3.80<br>Completion: 5.5 months<br>Success Score: 93.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: M<br>Funding: Sponsored",
          "Student ID: 2102-064/007<br>GPA: 3.50<br>Completion: 5.5 months<br>Success Score: 90.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-064/012<br>GPA: 2.60<br>Completion: 5.5 months<br>Success Score: 81.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-065A/005<br>GPA: 3.20<br>Completion: 1.0 months<br>Success Score: 87.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-065A/010<br>GPA: 3.50<br>Completion: 1.0 months<br>Success Score: 90.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-066/001<br>GPA: 3.20<br>Completion: 5.2 months<br>Success Score: 87.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-066/005<br>GPA: 3.20<br>Completion: 5.2 months<br>Success Score: 87.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-066/006<br>GPA: 3.70<br>Completion: 5.2 months<br>Success Score: 92.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-067A/008<br>GPA: 3.60<br>Completion: 2.6 months<br>Success Score: 91.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-068A/001<br>GPA: 2.90<br>Completion: 2.2 months<br>Success Score: 84.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: M<br>Funding: Sponsored",
          "Student ID: 2102-068A/005<br>GPA: 2.80<br>Completion: 2.2 months<br>Success Score: 83.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-069/001<br>GPA: 3.00<br>Completion: 5.0 months<br>Success Score: 85.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-069/008<br>GPA: 3.50<br>Completion: 5.0 months<br>Success Score: 90.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-069/009<br>GPA: 3.00<br>Completion: 5.0 months<br>Success Score: 85.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-069/011<br>GPA: 3.20<br>Completion: 5.0 months<br>Success Score: 87.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: M<br>Funding: Sponsored"
         ],
         "type": "scatter",
         "visible": true,
         "x": [
          16.98423127463863,
          16.98423127463863,
          16.98423127463863,
          16.95137976346912,
          16.95137976346912,
          16.95137976346912,
          17.04993429697766,
          17.04993429697766,
          16.98423127463863,
          16.98423127463863,
          16.98423127463863,
          16.95137976346912,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          4.993429697766097,
          4.993429697766097,
          2.3324572930354797,
          4.50065703022339,
          4.50065703022339,
          4.993429697766097,
          4.894875164257556,
          5.45335085413929,
          5.45335085413929,
          5.45335085413929,
          0.9855453350854139,
          0.9855453350854139,
          5.19053876478318,
          5.19053876478318,
          5.19053876478318,
          2.628120893561104,
          2.1681997371879107,
          2.1681997371879107,
          4.993429697766097,
          4.993429697766097,
          4.993429697766097,
          4.993429697766097
         ],
         "y": [
          2.9,
          2.1,
          2.9,
          2.1,
          3.9,
          3.7,
          3.6,
          3.4,
          2.6,
          2.1,
          2.9,
          3.9,
          3.8,
          2.2,
          3.6,
          3.4,
          2,
          3.7,
          2.8,
          3.9,
          2.8,
          3.4,
          3.2,
          2.7,
          3.8,
          3.5,
          2.6,
          3.2,
          3.5,
          3.2,
          3.2,
          3.7,
          3.6,
          2.9,
          2.8,
          3,
          3.5,
          3,
          3.2
         ]
        },
        {
         "hovertemplate": "%{text}<extra></extra>",
         "marker": {
          "color": [
           84,
           66,
           79,
           81,
           90,
           87,
           93,
           83,
           87,
           90
          ],
          "colorbar": {
           "len": 0.8,
           "tickfont": {
            "size": 10
           },
           "title": {
            "font": {
             "family": "Arial Black",
             "size": 12
            },
            "text": "Success<br>Score<br>(0-100)"
           }
          },
          "colorscale": [
           [
            0,
            "#440154"
           ],
           [
            0.1111111111111111,
            "#482878"
           ],
           [
            0.2222222222222222,
            "#3e4989"
           ],
           [
            0.3333333333333333,
            "#31688e"
           ],
           [
            0.4444444444444444,
            "#26828e"
           ],
           [
            0.5555555555555556,
            "#1f9e89"
           ],
           [
            0.6666666666666666,
            "#35b779"
           ],
           [
            0.7777777777777778,
            "#6ece58"
           ],
           [
            0.8888888888888888,
            "#b5de2b"
           ],
           [
            1,
            "#fde725"
           ]
          ],
          "line": {
           "color": "white",
           "width": 2
          },
          "opacity": 0.8,
          "showscale": false,
          "size": [
           12,
           16,
           16,
           12,
           12,
           12,
           12,
           12,
           12,
           12
          ],
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "SG PR (10 students)",
         "text": [
          "Student ID: 1101-009/011<br>GPA: 3.40<br>Completion: 17.0 months<br>Success Score: 84.0<br>Risk Category: Low Risk<br>Citizenship: SG PR<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 1101-012/004<br>GPA: 2.10<br>Completion: 17.0 months<br>Success Score: 66.0<br>Risk Category: Medium Risk<br>Citizenship: SG PR<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 1102-003/002<br>GPA: 3.40<br>Completion: 17.0 months<br>Success Score: 79.0<br>Risk Category: Medium Risk<br>Citizenship: SG PR<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-063/015<br>GPA: 2.60<br>Completion: 4.9 months<br>Success Score: 81.0<br>Risk Category: Low Risk<br>Citizenship: SG PR<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-064/014<br>GPA: 3.50<br>Completion: 5.5 months<br>Success Score: 90.0<br>Risk Category: Low Risk<br>Citizenship: SG PR<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-065A/001<br>GPA: 3.20<br>Completion: 1.0 months<br>Success Score: 87.0<br>Risk Category: Low Risk<br>Citizenship: SG PR<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-065A/009<br>GPA: 3.80<br>Completion: 1.0 months<br>Success Score: 93.0<br>Risk Category: Low Risk<br>Citizenship: SG PR<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-066/015<br>GPA: 2.80<br>Completion: 5.2 months<br>Success Score: 83.0<br>Risk Category: Low Risk<br>Citizenship: SG PR<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-067A/009<br>GPA: 3.20<br>Completion: 2.6 months<br>Success Score: 87.0<br>Risk Category: Low Risk<br>Citizenship: SG PR<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-068A/007<br>GPA: 3.50<br>Completion: 2.2 months<br>Success Score: 90.0<br>Risk Category: Low Risk<br>Citizenship: SG PR<br>Gender: F<br>Funding: Sponsored"
         ],
         "type": "scatter",
         "visible": true,
         "x": [
          16.98423127463863,
          17.04993429697766,
          17.04993429697766,
          4.894875164257556,
          5.45335085413929,
          0.9855453350854139,
          0.9855453350854139,
          5.19053876478318,
          2.628120893561104,
          2.1681997371879107
         ],
         "y": [
          3.4,
          2.1,
          3.4,
          2.6,
          3.5,
          3.2,
          3.8,
          2.8,
          3.2,
          3.5
         ]
        },
        {
         "hovertemplate": "%{text}<extra></extra>",
         "marker": {
          "color": [
           80,
           80,
           90,
           92,
           84,
           90,
           83
          ],
          "colorbar": {
           "len": 0.8,
           "tickfont": {
            "size": 10
           },
           "title": {
            "font": {
             "family": "Arial Black",
             "size": 12
            },
            "text": "Success<br>Score<br>(0-100)"
           }
          },
          "colorscale": [
           [
            0,
            "#440154"
           ],
           [
            0.1111111111111111,
            "#482878"
           ],
           [
            0.2222222222222222,
            "#3e4989"
           ],
           [
            0.3333333333333333,
            "#31688e"
           ],
           [
            0.4444444444444444,
            "#26828e"
           ],
           [
            0.5555555555555556,
            "#1f9e89"
           ],
           [
            0.6666666666666666,
            "#35b779"
           ],
           [
            0.7777777777777778,
            "#6ece58"
           ],
           [
            0.8888888888888888,
            "#b5de2b"
           ],
           [
            1,
            "#fde725"
           ]
          ],
          "line": {
           "color": "white",
           "width": 2
          },
          "opacity": 0.8,
          "showscale": false,
          "size": [
           16,
           16,
           12,
           12,
           12,
           12,
           12
          ],
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "FOREIGNER (7 students)",
         "text": [
          "Student ID: 1101-010/005<br>GPA: 3.50<br>Completion: 17.0 months<br>Success Score: 80.0<br>Risk Category: Medium Risk<br>Citizenship: FOREIGNER<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 1102-002/004<br>GPA: 3.50<br>Completion: 17.0 months<br>Success Score: 80.0<br>Risk Category: Medium Risk<br>Citizenship: FOREIGNER<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2101-108A/002<br>GPA: 3.50<br>Completion: 2.3 months<br>Success Score: 90.0<br>Risk Category: Low Risk<br>Citizenship: FOREIGNER<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2101-108A/007<br>GPA: 3.70<br>Completion: 2.3 months<br>Success Score: 92.0<br>Risk Category: Low Risk<br>Citizenship: FOREIGNER<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-066/004<br>GPA: 2.90<br>Completion: 5.2 months<br>Success Score: 84.0<br>Risk Category: Low Risk<br>Citizenship: FOREIGNER<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-069/002<br>GPA: 3.50<br>Completion: 5.0 months<br>Success Score: 90.0<br>Risk Category: Low Risk<br>Citizenship: FOREIGNER<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-070/004<br>GPA: 2.80<br>Completion: 5.0 months<br>Success Score: 83.0<br>Risk Category: Low Risk<br>Citizenship: FOREIGNER<br>Gender: F<br>Funding: Sponsored"
         ],
         "type": "scatter",
         "visible": true,
         "x": [
          16.95137976346912,
          16.95137976346912,
          2.3324572930354797,
          2.3324572930354797,
          5.19053876478318,
          4.993429697766097,
          4.993429697766097
         ],
         "y": [
          3.5,
          3.5,
          3.5,
          3.7,
          2.9,
          3.5,
          2.8
         ]
        },
        {
         "hovertemplate": "%{text}<extra></extra>",
         "marker": {
          "color": [
           92,
           94,
           91
          ],
          "colorscale": [
           [
            0,
            "#440154"
           ],
           [
            0.1111111111111111,
            "#482878"
           ],
           [
            0.2222222222222222,
            "#3e4989"
           ],
           [
            0.3333333333333333,
            "#31688e"
           ],
           [
            0.4444444444444444,
            "#26828e"
           ],
           [
            0.5555555555555556,
            "#1f9e89"
           ],
           [
            0.6666666666666666,
            "#35b779"
           ],
           [
            0.7777777777777778,
            "#6ece58"
           ],
           [
            0.8888888888888888,
            "#b5de2b"
           ],
           [
            1,
            "#fde725"
           ]
          ],
          "line": {
           "color": "white",
           "width": 2
          },
          "opacity": 0.8,
          "showscale": false,
          "size": [
           12,
           12,
           12
          ],
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "SG CITIZEN High Achievers (3 students)",
         "text": [
          "Student ID: 2101-107/003<br>GPA: 3.70 ⭐⭐<br>Completion: 5.0 months 🚀<br>Success Score: 92.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2101-108A/004<br>GPA: 3.90 ⭐⭐<br>Completion: 2.3 months 🚀<br>Success Score: 94.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 2102-067A/008<br>GPA: 3.60 ⭐⭐<br>Completion: 2.6 months 🚀<br>Success Score: 91.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored"
         ],
         "type": "scatter",
         "visible": false,
         "x": [
          4.993429697766097,
          2.3324572930354797,
          2.628120893561104
         ],
         "y": [
          3.7,
          3.9,
          3.6
         ]
        },
        {
         "hovertemplate": "%{text}<extra></extra>",
         "marker": {
          "color": [
           93
          ],
          "colorscale": [
           [
            0,
            "#440154"
           ],
           [
            0.1111111111111111,
            "#482878"
           ],
           [
            0.2222222222222222,
            "#3e4989"
           ],
           [
            0.3333333333333333,
            "#31688e"
           ],
           [
            0.4444444444444444,
            "#26828e"
           ],
           [
            0.5555555555555556,
            "#1f9e89"
           ],
           [
            0.6666666666666666,
            "#35b779"
           ],
           [
            0.7777777777777778,
            "#6ece58"
           ],
           [
            0.8888888888888888,
            "#b5de2b"
           ],
           [
            1,
            "#fde725"
           ]
          ],
          "line": {
           "color": "white",
           "width": 2
          },
          "opacity": 0.8,
          "showscale": false,
          "size": [
           12
          ],
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "SG PR High Achievers (1 students)",
         "text": [
          "Student ID: 2102-065A/009<br>GPA: 3.80 ⭐⭐<br>Completion: 1.0 months 🚀<br>Success Score: 93.0<br>Risk Category: Low Risk<br>Citizenship: SG PR<br>Gender: F<br>Funding: Sponsored"
         ],
         "type": "scatter",
         "visible": false,
         "x": [
          0.9855453350854139
         ],
         "y": [
          3.8
         ]
        },
        {
         "hovertemplate": "%{text}<extra></extra>",
         "marker": {
          "color": [
           92
          ],
          "colorscale": [
           [
            0,
            "#440154"
           ],
           [
            0.1111111111111111,
            "#482878"
           ],
           [
            0.2222222222222222,
            "#3e4989"
           ],
           [
            0.3333333333333333,
            "#31688e"
           ],
           [
            0.4444444444444444,
            "#26828e"
           ],
           [
            0.5555555555555556,
            "#1f9e89"
           ],
           [
            0.6666666666666666,
            "#35b779"
           ],
           [
            0.7777777777777778,
            "#6ece58"
           ],
           [
            0.8888888888888888,
            "#b5de2b"
           ],
           [
            1,
            "#fde725"
           ]
          ],
          "line": {
           "color": "white",
           "width": 2
          },
          "opacity": 0.8,
          "showscale": false,
          "size": [
           12
          ],
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "FOREIGNER High Achievers (1 students)",
         "text": [
          "Student ID: 2101-108A/007<br>GPA: 3.70 ⭐⭐<br>Completion: 2.3 months 🚀<br>Success Score: 92.0<br>Risk Category: Low Risk<br>Citizenship: FOREIGNER<br>Gender: F<br>Funding: Sponsored"
         ],
         "type": "scatter",
         "visible": false,
         "x": [
          2.3324572930354797
         ],
         "y": [
          3.7
         ]
        },
        {
         "hovertemplate": "%{text}<extra></extra>",
         "marker": {
          "color": [
           66,
           71,
           66,
           67,
           65
          ],
          "colorscale": [
           [
            0,
            "#440154"
           ],
           [
            0.1111111111111111,
            "#482878"
           ],
           [
            0.2222222222222222,
            "#3e4989"
           ],
           [
            0.3333333333333333,
            "#31688e"
           ],
           [
            0.4444444444444444,
            "#26828e"
           ],
           [
            0.5555555555555556,
            "#1f9e89"
           ],
           [
            0.6666666666666666,
            "#35b779"
           ],
           [
            0.7777777777777778,
            "#6ece58"
           ],
           [
            0.8888888888888888,
            "#b5de2b"
           ],
           [
            1,
            "#fde725"
           ]
          ],
          "line": {
           "color": "white",
           "width": 2
          },
          "opacity": 0.8,
          "showscale": false,
          "size": [
           16,
           12,
           16,
           16,
           16
          ],
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "SG CITIZEN Underperformers (5 students)",
         "text": [
          "Student ID: 1101-009/007<br>GPA: 2.10 🚨<br>Completion: 17.0 months<br>Success Score: 66.0<br>Risk Category: Medium Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 1101-010/002<br>GPA: 2.10 🚨<br>Completion: 17.0 months<br>Success Score: 71.0<br>Risk Category: Low Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 1102-001/005<br>GPA: 2.10 🚨<br>Completion: 17.0 months<br>Success Score: 66.0<br>Risk Category: Medium Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 1102-004/003<br>GPA: 2.20 🚨<br>Completion: 17.0 months<br>Success Score: 67.0<br>Risk Category: Medium Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored",
          "Student ID: 1102-004/008<br>GPA: 2.00 🚨<br>Completion: 17.0 months<br>Success Score: 65.0<br>Risk Category: Medium Risk<br>Citizenship: SG CITIZEN<br>Gender: F<br>Funding: Sponsored"
         ],
         "type": "scatter",
         "visible": false,
         "x": [
          16.98423127463863,
          16.95137976346912,
          16.98423127463863,
          17.04993429697766,
          17.04993429697766
         ],
         "y": [
          2.1,
          2.1,
          2.1,
          2.2,
          2
         ]
        },
        {
         "hovertemplate": "%{text}<extra></extra>",
         "marker": {
          "color": [
           66
          ],
          "colorscale": [
           [
            0,
            "#440154"
           ],
           [
            0.1111111111111111,
            "#482878"
           ],
           [
            0.2222222222222222,
            "#3e4989"
           ],
           [
            0.3333333333333333,
            "#31688e"
           ],
           [
            0.4444444444444444,
            "#26828e"
           ],
           [
            0.5555555555555556,
            "#1f9e89"
           ],
           [
            0.6666666666666666,
            "#35b779"
           ],
           [
            0.7777777777777778,
            "#6ece58"
           ],
           [
            0.8888888888888888,
            "#b5de2b"
           ],
           [
            1,
            "#fde725"
           ]
          ],
          "line": {
           "color": "white",
           "width": 2
          },
          "opacity": 0.8,
          "showscale": false,
          "size": [
           16
          ],
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "SG PR Underperformers (1 students)",
         "text": [
          "Student ID: 1101-012/004<br>GPA: 2.10 🚨<br>Completion: 17.0 months<br>Success Score: 66.0<br>Risk Category: Medium Risk<br>Citizenship: SG PR<br>Gender: F<br>Funding: Sponsored"
         ],
         "type": "scatter",
         "visible": false,
         "x": [
          17.04993429697766
         ],
         "y": [
          2.1
         ]
        },
        {
         "hovertemplate": "%{text}<extra></extra>",
         "marker": {
          "color": [],
          "colorscale": [
           [
            0,
            "#440154"
           ],
           [
            0.1111111111111111,
            "#482878"
           ],
           [
            0.2222222222222222,
            "#3e4989"
           ],
           [
            0.3333333333333333,
            "#31688e"
           ],
           [
            0.4444444444444444,
            "#26828e"
           ],
           [
            0.5555555555555556,
            "#1f9e89"
           ],
           [
            0.6666666666666666,
            "#35b779"
           ],
           [
            0.7777777777777778,
            "#6ece58"
           ],
           [
            0.8888888888888888,
            "#b5de2b"
           ],
           [
            1,
            "#fde725"
           ]
          ],
          "line": {
           "color": "white",
           "width": 2
          },
          "opacity": 0.8,
          "showscale": false,
          "size": [],
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "FOREIGNER Underperformers (0 students)",
         "text": [],
         "type": "scatter",
         "visible": false,
         "x": [],
         "y": []
        }
       ],
       "layout": {
        "annotations": [
         {
          "font": {
           "color": "#39FF14",
           "family": "Orbitron, monospace",
           "size": 12
          },
          "showarrow": false,
          "text": "🔍 Filter by Group:",
          "x": 0.02,
          "xref": "paper",
          "y": 1.18,
          "yref": "paper"
         },
         {
          "showarrow": false,
          "text": "Pass Threshold (2.0)",
          "x": 1,
          "xanchor": "right",
          "xref": "x domain",
          "y": 2,
          "yanchor": "bottom",
          "yref": "y"
         },
         {
          "showarrow": false,
          "text": "Excellence Threshold (3.5)",
          "x": 1,
          "xanchor": "right",
          "xref": "x domain",
          "y": 3.5,
          "yanchor": "bottom",
          "yref": "y"
         }
        ],
        "font": {
         "color": "#FFFFFF",
         "family": "Orbitron, monospace",
         "size": 12
        },
        "height": 700,
        "legend": {
         "bgcolor": "#1A1A2E",
         "bordercolor": "#00F5FF",
         "borderwidth": 1,
         "font": {
          "color": "#FFFFFF"
         },
         "orientation": "v",
         "x": 1.02,
         "xanchor": "left",
         "y": 0.98,
         "yanchor": "top"
        },
        "margin": {
         "b": 80,
         "l": 80,
         "r": 120,
         "t": 150
        },
        "paper_bgcolor": "#0A0A1A",
        "plot_bgcolor": "rgba(0,0,0,0)",
        "shapes": [
         {
          "line": {
           "color": "#EF4444",
           "dash": "dot",
           "width": 2
          },
          "opacity": 0.8,
          "type": "line",
          "x0": 0,
          "x1": 1,
          "xref": "x domain",
          "y0": 2,
          "y1": 2,
          "yref": "y"
         },
         {
          "line": {
           "color": "#10B981",
           "dash": "dot",
           "width": 2
          },
          "opacity": 0.8,
          "type": "line",
          "x0": 0,
          "x1": 1,
          "xref": "x domain",
          "y0": 3.5,
          "y1": 3.5,
          "yref": "y"
         },
         {
          "fillcolor": "rgba(16, 185, 129, 0.1)",
          "layer": "below",
          "line": {
           "width": 0
          },
          "type": "rect",
          "x0": 0,
          "x1": 1,
          "xref": "paper",
          "y0": 3.5,
          "y1": 4,
          "yref": "y"
         },
         {
          "fillcolor": "rgba(34, 211, 238, 0.1)",
          "layer": "below",
          "line": {
           "width": 0
          },
          "type": "rect",
          "x0": 0,
          "x1": 1,
          "xref": "paper",
          "y0": 2,
          "y1": 3.5,
          "yref": "y"
         },
         {
          "fillcolor": "rgba(239, 68, 68, 0.1)",
          "layer": "below",
          "line": {
           "width": 0
          },
          "type": "rect",
          "x0": 0,
          "x1": 1,
          "xref": "paper",
          "y0": 1,
          "y1": 2,
          "yref": "y"
         }
        ],
        "showlegend": true,
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "font": {
          "color": "#FFFFFF",
          "family": "Orbitron, monospace",
          "size": 20
         },
         "text": "<b>🎯 Interactive GPA vs Completion Time Analysis</b><br><sub>Success score by color • Risk level by marker size • Use filters to explore different groups</sub>",
         "x": 0.5,
         "y": 0.95
        },
        "updatemenus": [
         {
          "bgcolor": "#1A1A2E",
          "bordercolor": "#39FF14",
          "borderwidth": 2,
          "buttons": [
           {
            "args": [
             {
              "visible": [
               true,
               true,
               true,
               false,
               false,
               false,
               false,
               false,
               false
              ]
             }
            ],
            "label": "🌍 All Citizenship Types",
            "method": "update"
           },
           {
            "args": [
             {
              "visible": [
               true,
               false,
               false,
               false,
               false,
               false,
               false,
               false,
               false
              ]
             }
            ],
            "label": "🎯 SG CITIZEN Only",
            "method": "update"
           },
           {
            "args": [
             {
              "visible": [
               false,
               true,
               false,
               false,
               false,
               false,
               false,
               false,
               false
              ]
             }
            ],
            "label": "🎯 SG PR Only",
            "method": "update"
           },
           {
            "args": [
             {
              "visible": [
               false,
               false,
               true,
               false,
               false,
               false,
               false,
               false,
               false
              ]
             }
            ],
            "label": "🎯 FOREIGNER Only",
            "method": "update"
           },
           {
            "args": [
             {
              "visible": [
               false,
               false,
               false,
               true,
               true,
               true,
               false,
               false,
               false
              ]
             }
            ],
            "label": "⭐ High Achievers (GPA > 3.5 & < 5 months)",
            "method": "update"
           },
           {
            "args": [
             {
              "visible": [
               false,
               false,
               false,
               false,
               false,
               false,
               true,
               true,
               true
              ]
             }
            ],
            "label": "🚨 Underperformers (GPA < 2.5)",
            "method": "update"
           }
          ],
          "direction": "down",
          "font": {
           "color": "#FFFFFF"
          },
          "showactive": true,
          "x": 0.02,
          "xanchor": "left",
          "y": 1.12,
          "yanchor": "top"
         }
        ],
        "xaxis": {
         "gridcolor": "rgba(200,200,200,0.2)",
         "gridwidth": 1,
         "range": [
          0,
          22.04993429697766
         ],
         "tickfont": {
          "color": "#E2E8F0",
          "family": "Orbitron, monospace",
          "size": 12
         },
         "title": {
          "font": {
           "color": "#00F5FF",
           "family": "Orbitron, monospace",
           "size": 14
          },
          "text": "Completion Time (Months)"
         }
        },
        "yaxis": {
         "gridcolor": "rgba(200,200,200,0.2)",
         "gridwidth": 1,
         "range": [
          1,
          4
         ],
         "tickfont": {
          "color": "#E2E8F0",
          "family": "Orbitron, monospace",
          "size": 12
         },
         "title": {
          "font": {
           "color": "#BF40BF",
           "family": "Orbitron, monospace",
           "size": 14
          },
          "text": "Cumulative GPA"
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Chart 2 completed!\n"
     ]
    }
   ],
   "source": [
    "# === CHART 2: INTERACTIVE GPA vs COMPLETION TIME ANALYSIS ===\n",
    "print(\"🎨 Creating Chart 2: Interactive GPA vs Completion Time Analysis...\")\n",
    "\n",
    "# Prepare data for scatter plot analysis\n",
    "scatter_data = df.dropna(subset=['CUMULATIVE_GPA', 'COMPLETION_MONTHS', 'SUCCESS_SCORE'])\n",
    "\n",
    "# Create interactive scatter plot with multiple filtering options\n",
    "fig2 = go.Figure()\n",
    "\n",
    "# Create traces for each citizenship type (initially all visible)\n",
    "citizenship_types = scatter_data['CITIZENSHIP'].unique()\n",
    "for i, citizenship in enumerate(citizenship_types):\n",
    "    citizenship_subset = scatter_data[scatter_data['CITIZENSHIP'] == citizenship]\n",
    "    \n",
    "    fig2.add_trace(go.Scatter(\n",
    "        x=citizenship_subset['COMPLETION_MONTHS'],\n",
    "        y=citizenship_subset['CUMULATIVE_GPA'],\n",
    "        mode='markers',\n",
    "        marker=dict(\n",
    "            size=12 + (citizenship_subset['RISK_SCORE'] * 4),  # Size by risk score\n",
    "            color=citizenship_subset['SUCCESS_SCORE'],\n",
    "            colorscale='Viridis',\n",
    "            showscale=True if i == 0 else False,  # Show colorbar only once\n",
    "            colorbar=dict(\n",
    "                title=\"Success<br>Score<br>(0-100)\",\n",
    "                titlefont=dict(size=12, family='Arial Black'),\n",
    "                tickfont=dict(size=10),\n",
    "                len=0.8\n",
    "            ),\n",
    "            line=dict(width=2, color='white'),\n",
    "            opacity=0.8,\n",
    "            symbol='circle'\n",
    "        ),\n",
    "        text=[f\"Student ID: {row['STUDENT ID']}<br>\" +\n",
    "              f\"GPA: {row['CUMULATIVE_GPA']:.2f}<br>\" +\n",
    "              f\"Completion: {row['COMPLETION_MONTHS']:.1f} months<br>\" +\n",
    "              f\"Success Score: {row['SUCCESS_SCORE']:.1f}<br>\" +\n",
    "              f\"Risk Category: {row['RISK_CATEGORY']}<br>\" +\n",
    "              f\"Citizenship: {row['CITIZENSHIP']}<br>\" +\n",
    "              f\"Gender: {row['GENDER']}<br>\" +\n",
    "              f\"Funding: {row['COURSE FUNDING']}\"\n",
    "              for _, row in citizenship_subset.iterrows()],\n",
    "        hovertemplate='%{text}<extra></extra>',\n",
    "        name=f'{citizenship} ({len(citizenship_subset)} students)',\n",
    "        visible=True\n",
    "    ))\n",
    "\n",
    "# Add HIGH ACHIEVERS traces (GPA > 3.5 AND completion < 5 months) for each citizenship\n",
    "for i, citizenship in enumerate(citizenship_types):\n",
    "    high_achievers = scatter_data[(scatter_data['CITIZENSHIP'] == citizenship) & \n",
    "                                 (scatter_data['CUMULATIVE_GPA'] > 3.5) &\n",
    "                                 (scatter_data['COMPLETION_MONTHS'] < 5)]\n",
    "    \n",
    "    fig2.add_trace(go.Scatter(\n",
    "        x=high_achievers['COMPLETION_MONTHS'],\n",
    "        y=high_achievers['CUMULATIVE_GPA'],\n",
    "        mode='markers',\n",
    "        marker=dict(\n",
    "            size=12 + (high_achievers['RISK_SCORE'] * 4),\n",
    "            color=high_achievers['SUCCESS_SCORE'],\n",
    "            colorscale='Viridis',\n",
    "            showscale=False,\n",
    "            line=dict(width=2, color='white'),\n",
    "            opacity=0.8,\n",
    "            symbol='circle'\n",
    "        ),\n",
    "        text=[f\"Student ID: {row['STUDENT ID']}<br>\" +\n",
    "              f\"GPA: {row['CUMULATIVE_GPA']:.2f} ⭐⭐<br>\" +\n",
    "              f\"Completion: {row['COMPLETION_MONTHS']:.1f} months 🚀<br>\" +\n",
    "              f\"Success Score: {row['SUCCESS_SCORE']:.1f}<br>\" +\n",
    "              f\"Risk Category: {row['RISK_CATEGORY']}<br>\" +\n",
    "              f\"Citizenship: {row['CITIZENSHIP']}<br>\" +\n",
    "              f\"Gender: {row['GENDER']}<br>\" +\n",
    "              f\"Funding: {row['COURSE FUNDING']}\"\n",
    "              for _, row in high_achievers.iterrows()],\n",
    "        hovertemplate='%{text}<extra></extra>',\n",
    "        name=f'{citizenship} High Achievers ({len(high_achievers)} students)',\n",
    "        visible=False\n",
    "    ))\n",
    "\n",
    "# Add UNDERPERFORMERS traces (GPA < 2.5) for each citizenship\n",
    "for i, citizenship in enumerate(citizenship_types):\n",
    "    underperformers = scatter_data[(scatter_data['CITIZENSHIP'] == citizenship) & \n",
    "                                  (scatter_data['CUMULATIVE_GPA'] < 2.5)]\n",
    "    \n",
    "    fig2.add_trace(go.Scatter(\n",
    "        x=underperformers['COMPLETION_MONTHS'],\n",
    "        y=underperformers['CUMULATIVE_GPA'],\n",
    "        mode='markers',\n",
    "        marker=dict(\n",
    "            size=12 + (underperformers['RISK_SCORE'] * 4),\n",
    "            color=underperformers['SUCCESS_SCORE'],\n",
    "            colorscale='Viridis',\n",
    "            showscale=False,\n",
    "            line=dict(width=2, color='white'),\n",
    "            opacity=0.8,\n",
    "            symbol='circle'\n",
    "        ),\n",
    "        text=[f\"Student ID: {row['STUDENT ID']}<br>\" +\n",
    "              f\"GPA: {row['CUMULATIVE_GPA']:.2f} 🚨<br>\" +\n",
    "              f\"Completion: {row['COMPLETION_MONTHS']:.1f} months<br>\" +\n",
    "              f\"Success Score: {row['SUCCESS_SCORE']:.1f}<br>\" +\n",
    "              f\"Risk Category: {row['RISK_CATEGORY']}<br>\" +\n",
    "              f\"Citizenship: {row['CITIZENSHIP']}<br>\" +\n",
    "              f\"Gender: {row['GENDER']}<br>\" +\n",
    "              f\"Funding: {row['COURSE FUNDING']}\"\n",
    "              for _, row in underperformers.iterrows()],\n",
    "        hovertemplate='%{text}<extra></extra>',\n",
    "        name=f'{citizenship} Underperformers ({len(underperformers)} students)',\n",
    "        visible=False\n",
    "    ))\n",
    "\n",
    "# Create dropdown options for different views\n",
    "num_citizenship = len(citizenship_types)\n",
    "dropdown_buttons = [\n",
    "    # Show all citizenship types (regular view)\n",
    "    dict(label='🌍 All Citizenship Types', \n",
    "         method='update', \n",
    "         args=[{'visible': [True] * num_citizenship + [False] * (num_citizenship * 2)}]),\n",
    "]\n",
    "\n",
    "# Add individual citizenship options (regular view)\n",
    "for i, citizenship in enumerate(citizenship_types):\n",
    "    visibility = [False] * (num_citizenship * 3)  # Total traces = citizenship + high achievers + underperformers\n",
    "    visibility[i] = True  # Show only this citizenship's regular trace\n",
    "    dropdown_buttons.append(\n",
    "        dict(label=f'🎯 {citizenship} Only',\n",
    "             method='update',\n",
    "             args=[{'visible': visibility}])\n",
    "    )\n",
    "\n",
    "# Add high achievers view (show all high achiever traces)\n",
    "high_achiever_visibility = [False] * num_citizenship + [True] * num_citizenship + [False] * num_citizenship\n",
    "dropdown_buttons.append(\n",
    "    dict(label='⭐ High Achievers (GPA > 3.5 & < 5 months)', \n",
    "         method='update', \n",
    "         args=[{'visible': high_achiever_visibility}])\n",
    ")\n",
    "\n",
    "# Add underperformers view (show all underperformer traces)\n",
    "underperformer_visibility = [False] * (num_citizenship * 2) + [True] * num_citizenship\n",
    "dropdown_buttons.append(\n",
    "    dict(label='🚨 Underperformers (GPA < 2.5)', \n",
    "         method='update', \n",
    "         args=[{'visible': underperformer_visibility}])\n",
    ")\n",
    "\n",
    "# Configure layout with enhanced interactivity and proper filter positioning\n",
    "fig2.update_layout(\n",
    "    title=dict(\n",
    "        text='<b>🎯 Interactive GPA vs Completion Time Analysis</b><br>' +\n",
    "             '<sub>Success score by color • Risk level by marker size • Use filters to explore different groups</sub>',\n",
    "        font=dict(size=20, family='Orbitron, monospace', color=COLORS['light']),\n",
    "        x=0.5,\n",
    "        y=0.95\n",
    "    ),\n",
    "    xaxis=dict(\n",
    "        title=dict(text='Completion Time (Months)', font=dict(size=14, family='Orbitron, monospace', color=COLORS['neon_blue'])),\n",
    "        tickfont=dict(size=12, family='Orbitron, monospace', color=COLORS['text']),\n",
    "        gridcolor='rgba(200,200,200,0.2)',\n",
    "        gridwidth=1,\n",
    "        range=[0, max(scatter_data['COMPLETION_MONTHS']) + 5]\n",
    "    ),\n",
    "    yaxis=dict(\n",
    "        title=dict(text='Cumulative GPA', font=dict(size=14, family='Orbitron, monospace', color=COLORS['neon_purple'])),\n",
    "        tickfont=dict(size=12, family='Orbitron, monospace', color=COLORS['text']),\n",
    "        gridcolor='rgba(200,200,200,0.2)',\n",
    "        gridwidth=1,\n",
    "        range=[1.0, 4.0]\n",
    "    ),\n",
    "    font=dict(family='Orbitron, monospace', size=12, color=COLORS['light']),\n",
    "    paper_bgcolor=COLORS['dark_bg'],\n",
    "    plot_bgcolor='rgba(0,0,0,0)',\n",
    "    height=700,\n",
    "    margin=dict(t=150, l=80, r=120, b=80),\n",
    "    showlegend=True,\n",
    "    legend=dict(\n",
    "        orientation='v',\n",
    "        yanchor='top',\n",
    "        y=0.98,\n",
    "        xanchor='left',\n",
    "        x=1.02,\n",
    "        bgcolor=COLORS['card_bg'],\n",
    "        bordercolor=COLORS['neon_blue'],\n",
    "        borderwidth=1,\n",
    "        font=dict(color=COLORS['light'])\n",
    "    ),\n",
    "    \n",
    "    # Add interactive dropdown menu with proper positioning\n",
    "    updatemenus=[\n",
    "        dict(\n",
    "            buttons=dropdown_buttons,\n",
    "            direction=\"down\",\n",
    "            showactive=True,\n",
    "            x=0.02,\n",
    "            xanchor=\"left\",\n",
    "            y=1.12,\n",
    "            yanchor=\"top\",\n",
    "            bgcolor=COLORS['card_bg'],\n",
    "            bordercolor=COLORS['neon_green'],\n",
    "            borderwidth=2,\n",
    "            font=dict(color=COLORS['light'])\n",
    "        )\n",
    "    ],\n",
    "    \n",
    "    # Add filter label with proper positioning\n",
    "    annotations=[\n",
    "        dict(\n",
    "            text=\"🔍 Filter by Group:\",\n",
    "            x=0.02, y=1.18,\n",
    "            xref=\"paper\", yref=\"paper\",\n",
    "            showarrow=False,\n",
    "            font=dict(size=12, family='Orbitron, monospace', color=COLORS['neon_green'])\n",
    "        )\n",
    "    ]\n",
    ")\n",
    "\n",
    "# Add reference lines with dashboard colors\n",
    "fig2.add_hline(y=2.0, line_dash=\"dot\", line_color=COLORS['danger'], line_width=2, opacity=0.8, \n",
    "              annotation_text=\"Pass Threshold (2.0)\")\n",
    "fig2.add_hline(y=3.5, line_dash=\"dot\", line_color=COLORS['success'], line_width=2, opacity=0.8, \n",
    "              annotation_text=\"Excellence Threshold (3.5)\")\n",
    "\n",
    "# Add quadrant background shading with dashboard colors\n",
    "fig2.add_shape(type=\"rect\", xref=\"paper\", yref=\"y\", x0=0, y0=3.5, x1=1, y1=4.0,\n",
    "               fillcolor=f\"rgba({int(COLORS['success'][1:3], 16)}, {int(COLORS['success'][3:5], 16)}, {int(COLORS['success'][5:7], 16)}, 0.1)\", \n",
    "               layer=\"below\", line_width=0)\n",
    "fig2.add_shape(type=\"rect\", xref=\"paper\", yref=\"y\", x0=0, y0=2.0, x1=1, y1=3.5,\n",
    "               fillcolor=f\"rgba({int(COLORS['secondary'][1:3], 16)}, {int(COLORS['secondary'][3:5], 16)}, {int(COLORS['secondary'][5:7], 16)}, 0.1)\", \n",
    "               layer=\"below\", line_width=0)\n",
    "fig2.add_shape(type=\"rect\", xref=\"paper\", yref=\"y\", x0=0, y0=1.0, x1=1, y1=2.0,\n",
    "               fillcolor=f\"rgba({int(COLORS['danger'][1:3], 16)}, {int(COLORS['danger'][3:5], 16)}, {int(COLORS['danger'][5:7], 16)}, 0.1)\", \n",
    "               layer=\"below\", line_width=0)\n",
    "\n",
    "fig2.show()\n",
    "print(\"✅ Chart 2 completed!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "72586b6e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "🎨 Creating Chart 3: Interactive Completion Time Box Plot...\n"
     ]
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "boxpoints": "outliers",
         "hovertemplate": "<b>%{fullData.name}</b><br>Completion Time: %{y:.1f} months<br>Student Count: 33<br><extra></extra>",
         "jitter": 0.3,
         "marker": {
          "color": "#8B5FBF",
          "line": {
           "color": "white",
           "width": 1
          },
          "opacity": 0.6,
          "size": 4
         },
         "name": "FOREIGNER",
         "pointpos": -1.8,
         "type": "box",
         "visible": true,
         "y": [
          16.98423127463863,
          16.98423127463863,
          16.98423127463863,
          16.98423127463863,
          16.95137976346912,
          17.04993429697766,
          17.04993429697766,
          16.98423127463863,
          16.98423127463863,
          16.95137976346912,
          2.3324572930354797,
          2.3324572930354797,
          2.3324572930354797,
          4.50065703022339,
          4.894875164257556,
          5.45335085413929,
          5.45335085413929,
          0.9855453350854139,
          5.19053876478318,
          5.19053876478318,
          5.19053876478318,
          5.19053876478318,
          5.19053876478318,
          4.993429697766097,
          4.993429697766097,
          11.366622864651774,
          11.366622864651774,
          11.366622864651774,
          11.169513797634691,
          11.169513797634691,
          11.169513797634691,
          11.169513797634691,
          11.300919842312746
         ]
        },
        {
         "boxpoints": "outliers",
         "hovertemplate": "<b>%{fullData.name}</b><br>Completion Time: %{y:.1f} months<br>Student Count: 212<br><extra></extra>",
         "jitter": 0.3,
         "marker": {
          "color": "#22D3EE",
          "line": {
           "color": "white",
           "width": 1
          },
          "opacity": 0.6,
          "size": 4
         },
         "name": "SG CITIZEN",
         "pointpos": -1.8,
         "type": "box",
         "visible": true,
         "y": [
          16.98423127463863,
          16.98423127463863,
          16.98423127463863,
          22.996057818659658,
          16.98423127463863,
          16.95137976346912,
          16.95137976346912,
          16.95137976346912,
          16.95137976346912,
          16.95137976346912,
          16.95137976346912,
          16.95137976346912,
          16.95137976346912,
          16.95137976346912,
          16.95137976346912,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          16.98423127463863,
          16.98423127463863,
          22.996057818659658,
          16.98423127463863,
          16.98423127463863,
          16.95137976346912,
          16.95137976346912,
          16.95137976346912,
          16.95137976346912,
          16.95137976346912,
          16.95137976346912,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          17.04993429697766,
          4.993429697766097,
          4.993429697766097,
          4.993429697766097,
          4.993429697766097,
          4.993429697766097,
          4.993429697766097,
          4.993429697766097,
          2.3324572930354797,
          2.3324572930354797,
          2.3324572930354797,
          2.3324572930354797,
          2.3324572930354797,
          4.50065703022339,
          4.50065703022339,
          4.50065703022339,
          4.50065703022339,
          4.50065703022339,
          4.50065703022339,
          4.50065703022339,
          4.993429697766097,
          4.993429697766097,
          4.993429697766097,
          4.993429697766097,
          4.993429697766097,
          4.894875164257556,
          4.894875164257556,
          4.894875164257556,
          4.894875164257556,
          4.894875164257556,
          4.894875164257556,
          4.894875164257556,
          4.894875164257556,
          4.894875164257556,
          4.894875164257556,
          4.894875164257556,
          4.894875164257556,
          4.894875164257556,
          4.894875164257556,
          11.169513797634691,
          5.45335085413929,
          5.45335085413929,
          5.45335085413929,
          5.45335085413929,
          5.45335085413929,
          5.45335085413929,
          5.45335085413929,
          5.45335085413929,
          5.45335085413929,
          0.9855453350854139,
          0.9855453350854139,
          0.9855453350854139,
          0.9855453350854139,
          0.9855453350854139,
          0.9855453350854139,
          0.9855453350854139,
          5.19053876478318,
          5.19053876478318,
          5.19053876478318,
          5.19053876478318,
          5.19053876478318,
          5.19053876478318,
          5.19053876478318,
          5.19053876478318,
          2.628120893561104,
          2.628120893561104,
          2.628120893561104,
          2.628120893561104,
          2.628120893561104,
          2.628120893561104,
          2.628120893561104,
          2.628120893561104,
          2.1681997371879107,
          2.1681997371879107,
          2.1681997371879107,
          2.1681997371879107,
          2.1681997371879107,
          2.1681997371879107,
          2.1681997371879107,
          4.993429697766097,
          4.993429697766097,
          4.993429697766097,
          10.972404730617608,
          4.993429697766097,
          4.993429697766097,
          4.993429697766097,
          4.993429697766097,
          4.993429697766097,
          4.993429697766097,
          4.993429697766097,
          4.993429697766097,
          4.993429697766097,
          4.993429697766097,
          4.993429697766097,
          4.993429697766097,
          4.993429697766097,
          4.993429697766097,
          11.366622864651774,
          11.366622864651774,
          11.366622864651774,
          11.366622864651774,
          11.366622864651774,
          11.366622864651774,
          11.366622864651774,
          11.366622864651774,
          11.235216819973719,
          11.235216819973719,
          11.235216819973719,
          11.235216819973719,
          11.235216819973719,
          11.235216819973719,
          11.235216819973719,
          11.235216819973719,
          11.235216819973719,
          11.235216819973719,
          11.235216819973719,
          11.169513797634691,
          11.169513797634691,
          11.169513797634691,
          11.169513797634691,
          11.169513797634691,
          11.169513797634691,
          11.300919842312746,
          11.300919842312746,
          11.300919842312746,
          11.300919842312746,
          11.300919842312746,
          11.300919842312746,
          11.300919842312746,
          11.300919842312746,
          11.300919842312746,
          11.366622864651774,
          11.366622864651774,
          11.366622864651774,
          11.366622864651774,
          11.366622864651774,
          11.366622864651774,
          11.235216819973719,
          11.235216819973719,
          11.235216819973719,
          11.235216819973719,
          11.235216819973719,
          11.235216819973719,
          11.235216819973719,
          11.169513797634691,
          11.169513797634691,
          11.169513797634691,
          11.169513797634691,
          11.169513797634691,
          11.169513797634691,
          11.169513797634691,
          11.300919842312746,
          11.300919842312746,
          11.300919842312746,
          11.300919842312746,
          11.300919842312746
         ]
        },
        {
         "boxpoints": "outliers",
         "hovertemplate": "<b>%{fullData.name}</b><br>Completion Time: %{y:.1f} months<br>Student Count: 27<br><extra></extra>",
         "jitter": 0.3,
         "marker": {
          "color": "#F97316",
          "line": {
           "color": "white",
           "width": 1
          },
          "opacity": 0.6,
          "size": 4
         },
         "name": "SG PR",
         "pointpos": -1.8,
         "type": "box",
         "visible": true,
         "y": [
          16.98423127463863,
          16.98423127463863,
          16.95137976346912,
          17.04993429697766,
          16.98423127463863,
          17.04993429697766,
          4.993429697766097,
          4.993429697766097,
          4.894875164257556,
          5.45335085413929,
          5.45335085413929,
          0.9855453350854139,
          0.9855453350854139,
          0.9855453350854139,
          0.9855453350854139,
          5.19053876478318,
          5.19053876478318,
          2.628120893561104,
          2.628120893561104,
          2.1681997371879107,
          2.1681997371879107,
          4.993429697766097,
          4.993429697766097,
          11.366622864651774,
          11.169513797634691,
          11.300919842312746,
          11.366622864651774
         ]
        }
       ],
       "layout": {
        "annotations": [
         {
          "font": {
           "color": "#BF40BF",
           "family": "Orbitron, monospace",
           "size": 12
          },
          "showarrow": false,
          "text": "🔍 Filter Options:",
          "x": 0.02,
          "xref": "paper",
          "y": 1.18,
          "yref": "paper"
         }
        ],
        "font": {
         "color": "#FFFFFF",
         "family": "Orbitron, monospace",
         "size": 12
        },
        "height": 700,
        "margin": {
         "b": 80,
         "l": 80,
         "r": 80,
         "t": 150
        },
        "paper_bgcolor": "#0A0A1A",
        "plot_bgcolor": "rgba(0,0,0,0)",
        "showlegend": false,
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "font": {
          "color": "#FFFFFF",
          "size": 18
         },
         "text": "<b>🔍 Course Completion Time Distribution</b><br><sub>Interactive box plot analysis of completion duration by citizenship status</sub>",
         "x": 0.5
        },
        "updatemenus": [
         {
          "bgcolor": "#1A1A2E",
          "bordercolor": "#BF40BF",
          "borderwidth": 2,
          "buttons": [
           {
            "args": [
             {
              "visible": [
               true,
               true,
               true
              ]
             }
            ],
            "label": "All Citizenship Types",
            "method": "update"
           },
           {
            "args": [
             {
              "visible": [
               true,
               false,
               false
              ]
             }
            ],
            "label": "FOREIGNER Only",
            "method": "update"
           },
           {
            "args": [
             {
              "visible": [
               false,
               true,
               false
              ]
             }
            ],
            "label": "SG CITIZEN Only",
            "method": "update"
           },
           {
            "args": [
             {
              "visible": [
               false,
               false,
               true
              ]
             }
            ],
            "label": "SG PR Only",
            "method": "update"
           }
          ],
          "direction": "down",
          "font": {
           "color": "#FFFFFF"
          },
          "showactive": true,
          "x": 0.02,
          "xanchor": "left",
          "y": 1.12,
          "yanchor": "top"
         }
        ],
        "xaxis": {
         "gridcolor": "rgba(200,200,200,0.2)",
         "gridwidth": 1,
         "tickfont": {
          "color": "#E2E8F0"
         },
         "title": {
          "font": {
           "color": "#00F5FF"
          },
          "text": "Citizenship Status"
         }
        },
        "yaxis": {
         "gridcolor": "rgba(200,200,200,0.2)",
         "gridwidth": 1,
         "range": [
          0,
          60
         ],
         "tickfont": {
          "color": "#E2E8F0"
         },
         "title": {
          "font": {
           "color": "#39FF14"
          },
          "text": "Completion Time (Months)"
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Chart 3 completed!\n"
     ]
    }
   ],
   "source": [
    "# === CHART 3: INTERACTIVE BOX PLOT - COMPLETION TIME ANALYSIS ===\n",
    "print(\"🎨 Creating Chart 3: Interactive Completion Time Box Plot...\")\n",
    "\n",
    "# Filter out invalid completion times\n",
    "completion_data = df.dropna(subset=['COMPLETION_MONTHS'])\n",
    "completion_data = completion_data[completion_data['COMPLETION_MONTHS'] > 0]\n",
    "completion_data = completion_data[completion_data['COMPLETION_MONTHS'] <= 60]  # Reasonable max of 5 years\n",
    "\n",
    "fig3 = go.Figure()\n",
    "\n",
    "# Add box plot for all citizenship types\n",
    "for i, citizenship in enumerate(completion_data['CITIZENSHIP'].unique()):\n",
    "    citizenship_data = completion_data[completion_data['CITIZENSHIP'] == citizenship]\n",
    "    \n",
    "    fig3.add_trace(\n",
    "        go.Box(\n",
    "            y=citizenship_data['COMPLETION_MONTHS'],\n",
    "            name=citizenship,\n",
    "            marker_color=citizenship_colors[i % len(citizenship_colors)],\n",
    "            boxpoints='outliers',  # Show outliers\n",
    "            jitter=0.3,  # Add some jitter to points\n",
    "            pointpos=-1.8,  # Position of points\n",
    "            marker=dict(\n",
    "                size=4,\n",
    "                opacity=0.6,\n",
    "                line=dict(width=1, color='white')\n",
    "            ),\n",
    "            hovertemplate='<b>%{fullData.name}</b><br>' +\n",
    "                         'Completion Time: %{y:.1f} months<br>' +\n",
    "                         'Student Count: ' + str(len(citizenship_data)) + '<br>' +\n",
    "                         '<extra></extra>',\n",
    "            visible=True\n",
    "        )\n",
    "    )\n",
    "\n",
    "# Add \"All Categories\" option (show all)\n",
    "all_visible = [True] * len(completion_data['CITIZENSHIP'].unique())\n",
    "\n",
    "# Create dropdown options\n",
    "dropdown_buttons = [\n",
    "    dict(label='All Citizenship Types',\n",
    "         method='update',\n",
    "         args=[{'visible': all_visible}])\n",
    "]\n",
    "\n",
    "# Add individual citizenship type options\n",
    "for i, citizenship in enumerate(completion_data['CITIZENSHIP'].unique()):\n",
    "    visibility = [False] * len(completion_data['CITIZENSHIP'].unique())\n",
    "    visibility[i] = True\n",
    "    dropdown_buttons.append(\n",
    "        dict(label=f'{citizenship} Only',\n",
    "             method='update',\n",
    "             args=[{'visible': visibility}])\n",
    "    )\n",
    "\n",
    "fig3.update_layout(\n",
    "    title='<b>🔍 Course Completion Time Distribution</b><br><sub>Interactive box plot analysis of completion duration by citizenship status</sub>',\n",
    "    title_font_size=18,\n",
    "    title_x=0.5,\n",
    "    title_font_color=COLORS['light'],\n",
    "    yaxis_title='Completion Time (Months)',\n",
    "    xaxis_title='Citizenship Status',\n",
    "    font=dict(family='Orbitron, monospace', size=12, color=COLORS['light']),\n",
    "    paper_bgcolor=COLORS['dark_bg'],\n",
    "    plot_bgcolor='rgba(0,0,0,0)',\n",
    "    height=700,\n",
    "    margin=dict(t=150, l=80, r=80, b=80),\n",
    "    showlegend=False,\n",
    "    updatemenus=[\n",
    "        dict(\n",
    "            buttons=dropdown_buttons,\n",
    "            direction='down',\n",
    "            showactive=True,\n",
    "            x=0.02,\n",
    "            xanchor='left',\n",
    "            y=1.12,\n",
    "            yanchor='top',\n",
    "            bgcolor=COLORS['card_bg'],\n",
    "            bordercolor=COLORS['neon_purple'],\n",
    "            borderwidth=2,\n",
    "            font=dict(color=COLORS['light'])\n",
    "        )\n",
    "    ],\n",
    "    annotations=[\n",
    "        dict(\n",
    "            text=\"🔍 Filter Options:\",\n",
    "            x=0.02, y=1.18,\n",
    "            xref=\"paper\", yref=\"paper\",\n",
    "            showarrow=False,\n",
    "            font=dict(size=12, family='Orbitron, monospace', color=COLORS['neon_purple'])\n",
    "        )\n",
    "    ]\n",
    ")\n",
    "\n",
    "# Add grid lines for better readability with dashboard theme\n",
    "fig3.update_layout(\n",
    "    yaxis=dict(\n",
    "        gridcolor='rgba(200,200,200,0.2)',\n",
    "        gridwidth=1,\n",
    "        range=[0, 60],\n",
    "        title_font_color=COLORS['neon_green'],\n",
    "        tickfont=dict(color=COLORS['text'])\n",
    "    ),\n",
    "    xaxis=dict(\n",
    "        gridcolor='rgba(200,200,200,0.2)',\n",
    "        gridwidth=1,\n",
    "        title_font_color=COLORS['neon_blue'],\n",
    "        tickfont=dict(color=COLORS['text'])\n",
    "    )\n",
    ")\n",
    "\n",
    "fig3.show()\n",
    "print(\"✅ Chart 3 completed!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4dbb104c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "🎨 Creating Chart 4: Animated GPA Performance Trends...\n"
     ]
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "connectgaps": true,
         "customdata": [
          34,
          227,
          29
         ],
         "hovertemplate": "<b>%{x}</b><br>Average GPA: %{y:.2f}<br>Students: %{customdata}<br>Period: Semester 1<extra></extra>",
         "line": {
          "color": "#8B5FBF",
          "shape": "spline",
          "smoothing": 0.3,
          "width": 4
         },
         "marker": {
          "color": [
           "#8B5FBF",
           "#22D3EE",
           "#F97316"
          ],
          "line": {
           "color": "white",
           "width": 3
          },
          "opacity": 0.8,
          "size": [
           26.8,
           65.4,
           25.8
          ],
          "symbol": "circle"
         },
         "mode": "markers+lines+text",
         "name": "Semester 1",
         "text": [
          "3.34",
          "3.05",
          "2.98"
         ],
         "textfont": {
          "color": "#E2E8F0",
          "family": "Arial Black",
          "size": 14
         },
         "textposition": "top center",
         "type": "scatter",
         "x": [
          "FOREIGNER",
          "SG CITIZEN",
          "SG PR"
         ],
         "y": [
          3.34,
          3.05,
          2.98
         ]
        }
       ],
       "frames": [
        {
         "data": [
          {
           "connectgaps": true,
           "customdata": [
            34,
            227,
            29
           ],
           "hovertemplate": "<b>%{x}</b><br>Average GPA: %{y:.2f}<br>Students: %{customdata}<br>Period: Semester 1<extra></extra>",
           "line": {
            "color": "#8B5FBF",
            "shape": "spline",
            "smoothing": 0.3,
            "width": 4
           },
           "marker": {
            "color": [
             "#8B5FBF",
             "#22D3EE",
             "#F97316"
            ],
            "line": {
             "color": "white",
             "width": 3
            },
            "opacity": 0.8,
            "size": [
             26.8,
             65.4,
             25.8
            ],
            "symbol": "circle"
           },
           "mode": "markers+lines+text",
           "name": "Semester 1",
           "text": [
            "3.34",
            "3.05",
            "2.98"
           ],
           "textfont": {
            "color": "#E2E8F0",
            "family": "Arial Black",
            "size": 14
           },
           "textposition": "top center",
           "type": "scatter",
           "x": [
            "FOREIGNER",
            "SG CITIZEN",
            "SG PR"
           ],
           "y": [
            3.34,
            3.05,
            2.98
           ]
          }
         ],
         "name": "Semester 1"
        },
        {
         "data": [
          {
           "connectgaps": true,
           "customdata": [
            18,
            125,
            11
           ],
           "hovertemplate": "<b>%{x}</b><br>Average GPA: %{y:.2f}<br>Students: %{customdata}<br>Period: Semester 2<extra></extra>",
           "line": {
            "color": "#8B5FBF",
            "shape": "spline",
            "smoothing": 0.3,
            "width": 4
           },
           "marker": {
            "color": [
             "#8B5FBF",
             "#22D3EE",
             "#F97316"
            ],
            "line": {
             "color": "white",
             "width": 3
            },
            "opacity": 0.8,
            "size": [
             23.6,
             45,
             22.2
            ],
            "symbol": "circle"
           },
           "mode": "markers+lines+text",
           "name": "Semester 2",
           "text": [
            "3.37",
            "3.11",
            "2.78"
           ],
           "textfont": {
            "color": "#E2E8F0",
            "family": "Arial Black",
            "size": 14
           },
           "textposition": "top center",
           "type": "scatter",
           "x": [
            "FOREIGNER",
            "SG CITIZEN",
            "SG PR"
           ],
           "y": [
            3.37,
            3.11,
            2.78
           ]
          }
         ],
         "name": "Semester 2"
        },
        {
         "data": [
          {
           "connectgaps": true,
           "customdata": [
            10,
            64,
            7
           ],
           "hovertemplate": "<b>%{x}</b><br>Average GPA: %{y:.2f}<br>Students: %{customdata}<br>Period: Semester 3<extra></extra>",
           "line": {
            "color": "#8B5FBF",
            "shape": "spline",
            "smoothing": 0.3,
            "width": 4
           },
           "marker": {
            "color": [
             "#8B5FBF",
             "#22D3EE",
             "#F97316"
            ],
            "line": {
             "color": "white",
             "width": 3
            },
            "opacity": 0.8,
            "size": [
             22,
             32.8,
             21.4
            ],
            "symbol": "circle"
           },
           "mode": "markers+lines+text",
           "name": "Semester 3",
           "text": [
            "3.67",
            "3.26",
            "3.20"
           ],
           "textfont": {
            "color": "#E2E8F0",
            "family": "Arial Black",
            "size": 14
           },
           "textposition": "top center",
           "type": "scatter",
           "x": [
            "FOREIGNER",
            "SG CITIZEN",
            "SG PR"
           ],
           "y": [
            3.67,
            3.26,
            3.2
           ]
          }
         ],
         "name": "Semester 3"
        }
       ],
       "layout": {
        "annotations": [
         {
          "font": {
           "color": "#39FF14",
           "family": "Orbitron, monospace",
           "size": 12
          },
          "showarrow": false,
          "text": "🎬 Animation Controls:",
          "x": 0.02,
          "xref": "paper",
          "y": 1.18,
          "yref": "paper"
         },
         {
          "showarrow": false,
          "text": "🎯 Pass Threshold (2.0)",
          "x": 1,
          "xanchor": "right",
          "xref": "x domain",
          "y": 2,
          "yanchor": "bottom",
          "yref": "y"
         },
         {
          "showarrow": false,
          "text": "🌟 Excellence Threshold (3.0)",
          "x": 1,
          "xanchor": "right",
          "xref": "x domain",
          "y": 3,
          "yanchor": "top",
          "yref": "y"
         }
        ],
        "font": {
         "color": "#FFFFFF",
         "family": "Orbitron, monospace",
         "size": 12
        },
        "height": 700,
        "margin": {
         "b": 80,
         "l": 90,
         "r": 90,
         "t": 150
        },
        "paper_bgcolor": "#0A0A1A",
        "plot_bgcolor": "rgba(0,0,0,0)",
        "shapes": [
         {
          "line": {
           "color": "#EF4444",
           "dash": "dot",
           "width": 3
          },
          "type": "line",
          "x0": 0,
          "x1": 1,
          "xref": "x domain",
          "y0": 2,
          "y1": 2,
          "yref": "y"
         },
         {
          "line": {
           "color": "#10B981",
           "dash": "dot",
           "width": 3
          },
          "type": "line",
          "x0": 0,
          "x1": 1,
          "xref": "x domain",
          "y0": 3,
          "y1": 3,
          "yref": "y"
         },
         {
          "fillcolor": "rgba(16, 185, 129, 0.1)",
          "layer": "below",
          "line": {
           "width": 0
          },
          "type": "rect",
          "x0": 0,
          "x1": 1,
          "xref": "paper",
          "y0": 3,
          "y1": 4,
          "yref": "y"
         },
         {
          "fillcolor": "rgba(52, 152, 219, 0.1)",
          "layer": "below",
          "line": {
           "width": 0
          },
          "type": "rect",
          "x0": 0,
          "x1": 1,
          "xref": "paper",
          "y0": 2,
          "y1": 3,
          "yref": "y"
         },
         {
          "fillcolor": "rgba(231, 76, 60, 0.1)",
          "layer": "below",
          "line": {
           "width": 0
          },
          "type": "rect",
          "x0": 0,
          "x1": 1,
          "xref": "paper",
          "y0": 1.5,
          "y1": 2,
          "yref": "y"
         }
        ],
        "showlegend": false,
        "sliders": [
         {
          "active": 0,
          "bgcolor": "rgba(255,255,255,0.9)",
          "bordercolor": "#6C7B7F",
          "borderwidth": 1,
          "currentvalue": {
           "font": {
            "family": "Arial Black",
            "size": 16
           },
           "prefix": "📅 Current Period: ",
           "visible": true,
           "xanchor": "center"
          },
          "len": 0.85,
          "pad": {
           "b": 10,
           "t": 60
          },
          "steps": [
           {
            "args": [
             [
              "Semester 1"
             ],
             {
              "frame": {
               "duration": 400,
               "redraw": true
              },
              "mode": "immediate",
              "transition": {
               "duration": 400,
               "easing": "cubic-in-out"
              }
             }
            ],
            "label": "Semester 1",
            "method": "animate",
            "value": "Semester 1"
           },
           {
            "args": [
             [
              "Semester 2"
             ],
             {
              "frame": {
               "duration": 400,
               "redraw": true
              },
              "mode": "immediate",
              "transition": {
               "duration": 400,
               "easing": "cubic-in-out"
              }
             }
            ],
            "label": "Semester 2",
            "method": "animate",
            "value": "Semester 2"
           },
           {
            "args": [
             [
              "Semester 3"
             ],
             {
              "frame": {
               "duration": 400,
               "redraw": true
              },
              "mode": "immediate",
              "transition": {
               "duration": 400,
               "easing": "cubic-in-out"
              }
             }
            ],
            "label": "Semester 3",
            "method": "animate",
            "value": "Semester 3"
           }
          ],
          "tickcolor": "#8B5FBF",
          "transition": {
           "duration": 400,
           "easing": "cubic-in-out"
          },
          "x": 0.075,
          "xanchor": "left",
          "y": -0.05,
          "yanchor": "top"
         }
        ],
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "font": {
          "color": "#FFFFFF",
          "family": "Orbitron, monospace",
          "size": 20
         },
         "text": "<b>📈 Academic Performance Evolution Over Time</b><br><sub>Average GPA trends by citizenship status across semesters</sub><br><span style=\"font-size:12px; color:#94A3B8;\">💡 Marker size reflects student count | Only periods with 3+ students shown</span>",
         "x": 0.5,
         "y": 0.95
        },
        "updatemenus": [
         {
          "bgcolor": "#1A1A2E",
          "bordercolor": "#39FF14",
          "borderwidth": 2,
          "buttons": [
           {
            "args": [
             null,
             {
              "frame": {
               "duration": 1200,
               "redraw": true
              },
              "fromcurrent": true,
              "transition": {
               "duration": 400,
               "easing": "cubic-in-out"
              }
             }
            ],
            "label": "▶️ Play Animation",
            "method": "animate"
           },
           {
            "args": [
             [
              null
             ],
             {
              "frame": {
               "duration": 0,
               "redraw": false
              },
              "mode": "immediate"
             }
            ],
            "label": "⏸️ Pause",
            "method": "animate"
           },
           {
            "args": [
             null,
             {
              "frame": {
               "duration": 1200,
               "redraw": true
              },
              "fromcurrent": false,
              "transition": {
               "duration": 400,
               "easing": "cubic-in-out"
              }
             }
            ],
            "label": "🔄 Restart",
            "method": "animate"
           }
          ],
          "font": {
           "color": "#FFFFFF"
          },
          "showactive": false,
          "type": "buttons",
          "x": 0.02,
          "xanchor": "left",
          "y": 1.12,
          "yanchor": "top"
         }
        ],
        "xaxis": {
         "gridcolor": "rgba(200,200,200,0.2)",
         "gridwidth": 1,
         "linecolor": "#94A3B8",
         "linewidth": 2,
         "showline": true,
         "tickfont": {
          "color": "#E2E8F0",
          "family": "Orbitron, monospace",
          "size": 12
         },
         "title": {
          "font": {
           "color": "#00F5FF",
           "family": "Orbitron, monospace",
           "size": 14
          },
          "text": "Citizenship Status"
         }
        },
        "yaxis": {
         "dtick": 0.25,
         "gridcolor": "rgba(200,200,200,0.2)",
         "gridwidth": 1,
         "linecolor": "#94A3B8",
         "linewidth": 2,
         "range": [
          1.5,
          4
         ],
         "showline": true,
         "tick0": 1.5,
         "tickfont": {
          "color": "#E2E8F0",
          "family": "Orbitron, monospace",
          "size": 12
         },
         "tickmode": "linear",
         "title": {
          "font": {
           "color": "#BF40BF",
           "family": "Orbitron, monospace",
           "size": 14
          },
          "text": "Average GPA"
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Chart 4 completed!\n"
     ]
    }
   ],
   "source": [
    "# === CHART 4: ANIMATED GPA TRENDS OVER TIME ===\n",
    "print(\"🎨 Creating Chart 4: Animated GPA Performance Trends...\")\n",
    "\n",
    "# Use the existing period_data which has semester GPA information\n",
    "gpa_trends = period_data.groupby(['PERIOD', 'CITIZENSHIP'], as_index=False).agg({\n",
    "    'GPA': ['mean', 'count']\n",
    "}).round(2)\n",
    "\n",
    "# Flatten column names\n",
    "gpa_trends.columns = ['PERIOD', 'CITIZENSHIP', 'AVG_GPA', 'STUDENT_COUNT']\n",
    "\n",
    "# Filter out periods/citizenship combinations with very few students (less than 3)\n",
    "gpa_trends = gpa_trends[gpa_trends['STUDENT_COUNT'] >= 3]\n",
    "\n",
    "# Get unique periods and citizenship types for consistent animation\n",
    "periods = sorted(gpa_trends['PERIOD'].unique())\n",
    "citizenship_types = sorted(gpa_trends['CITIZENSHIP'].unique())\n",
    "\n",
    "# Create frames for animation with enhanced visuals\n",
    "frames = []\n",
    "for period in periods:\n",
    "    period_frame = gpa_trends[gpa_trends['PERIOD'] == period]\n",
    "    \n",
    "    if len(period_frame) > 0:  # Only create frame if data exists\n",
    "        frames.append(\n",
    "            go.Frame(\n",
    "                data=[\n",
    "                    go.Scatter(\n",
    "                        x=period_frame['CITIZENSHIP'],\n",
    "                        y=period_frame['AVG_GPA'],\n",
    "                        mode='markers+lines+text',\n",
    "                        marker=dict(\n",
    "                            size=[20 + (count/5) for count in period_frame['STUDENT_COUNT']],  # Size based on student count\n",
    "                            color=citizenship_colors[:len(period_frame)],\n",
    "                            line=dict(width=3, color='white'),\n",
    "                            opacity=0.8,\n",
    "                            symbol='circle'\n",
    "                        ),\n",
    "                        line=dict(\n",
    "                            width=4, \n",
    "                            color=COLORS['primary'],\n",
    "                            shape='spline',  # Smooth curved lines\n",
    "                            smoothing=0.3\n",
    "                        ),\n",
    "                        text=[f\"{gpa:.2f}\" for gpa in period_frame['AVG_GPA']],\n",
    "                        textposition='top center',\n",
    "                        textfont=dict(size=14, color=COLORS['text'], family='Arial Black'),\n",
    "                        hovertemplate='<b>%{x}</b><br>' +\n",
    "                                    'Average GPA: %{y:.2f}<br>' +\n",
    "                                    'Students: %{customdata}<br>' +\n",
    "                                    'Period: ' + period + '<extra></extra>',\n",
    "                        customdata=period_frame['STUDENT_COUNT'],\n",
    "                        name=period,\n",
    "                        connectgaps=True\n",
    "                    )\n",
    "                ],\n",
    "                name=period\n",
    "            )\n",
    "        )\n",
    "\n",
    "# Create initial frame with better styling\n",
    "if len(periods) > 0:\n",
    "    initial_period_data = gpa_trends[gpa_trends['PERIOD'] == periods[0]]\n",
    "    \n",
    "    fig4 = go.Figure(\n",
    "        data=[\n",
    "            go.Scatter(\n",
    "                x=initial_period_data['CITIZENSHIP'],\n",
    "                y=initial_period_data['AVG_GPA'],\n",
    "                mode='markers+lines+text',\n",
    "                marker=dict(\n",
    "                    size=[20 + (count/5) for count in initial_period_data['STUDENT_COUNT']],\n",
    "                    color=citizenship_colors[:len(initial_period_data)],\n",
    "                    line=dict(width=3, color='white'),\n",
    "                    opacity=0.8,\n",
    "                    symbol='circle'\n",
    "                ),\n",
    "                line=dict(\n",
    "                    width=4, \n",
    "                    color=COLORS['primary'],\n",
    "                    shape='spline',\n",
    "                    smoothing=0.3\n",
    "                ),\n",
    "                text=[f\"{gpa:.2f}\" for gpa in initial_period_data['AVG_GPA']],\n",
    "                textposition='top center',\n",
    "                textfont=dict(size=14, color=COLORS['text'], family='Arial Black'),\n",
    "                hovertemplate='<b>%{x}</b><br>' +\n",
    "                            'Average GPA: %{y:.2f}<br>' +\n",
    "                            'Students: %{customdata}<br>' +\n",
    "                            'Period: ' + periods[0] + '<extra></extra>',\n",
    "                customdata=initial_period_data['STUDENT_COUNT'],\n",
    "                name=periods[0],\n",
    "                connectgaps=True\n",
    "            )\n",
    "        ],\n",
    "        frames=frames\n",
    "    )\n",
    "\n",
    "    # Enhanced layout with dashboard theme\n",
    "    fig4.update_layout(\n",
    "        title=dict(\n",
    "            text='<b>📈 Academic Performance Evolution Over Time</b><br>' +\n",
    "                 '<sub>Average GPA trends by citizenship status across semesters</sub><br>' +\n",
    "                 '<span style=\"font-size:12px; color:' + COLORS['text_dim'] + ';\">💡 Marker size reflects student count | Only periods with 3+ students shown</span>',\n",
    "            font=dict(size=20, family='Orbitron, monospace', color=COLORS['light']),\n",
    "            x=0.5,\n",
    "            y=0.95\n",
    "        ),\n",
    "        xaxis=dict(\n",
    "            title=dict(text='Citizenship Status', font=dict(size=14, family='Orbitron, monospace', color=COLORS['neon_blue'])),\n",
    "            gridcolor='rgba(200,200,200,0.2)',\n",
    "            gridwidth=1,\n",
    "            showline=True,\n",
    "            linewidth=2,\n",
    "            linecolor=COLORS['text_dim'],\n",
    "            tickfont=dict(size=12, family='Orbitron, monospace', color=COLORS['text'])\n",
    "        ),\n",
    "        yaxis=dict(\n",
    "            title=dict(text='Average GPA', font=dict(size=14, family='Orbitron, monospace', color=COLORS['neon_purple'])),\n",
    "            range=[1.5, 4.0], \n",
    "            gridcolor='rgba(200,200,200,0.2)', \n",
    "            gridwidth=1,\n",
    "            tickmode='linear',\n",
    "            tick0=1.5,\n",
    "            dtick=0.25,\n",
    "            showline=True,\n",
    "            linewidth=2,\n",
    "            linecolor=COLORS['text_dim'],\n",
    "            tickfont=dict(size=12, family='Orbitron, monospace', color=COLORS['text'])\n",
    "        ),\n",
    "        font=dict(family='Orbitron, monospace', size=12, color=COLORS['light']),\n",
    "        paper_bgcolor=COLORS['dark_bg'],\n",
    "        plot_bgcolor='rgba(0,0,0,0)',\n",
    "        height=700,\n",
    "        margin=dict(t=150, l=90, r=90, b=80),\n",
    "        showlegend=False,\n",
    "        \n",
    "        # Enhanced animation controls with dashboard theme\n",
    "        updatemenus=[\n",
    "            dict(\n",
    "                type='buttons',\n",
    "                showactive=False,\n",
    "                x=0.02,\n",
    "                xanchor='left',\n",
    "                y=1.12,\n",
    "                yanchor='top',\n",
    "                bgcolor=COLORS['card_bg'],\n",
    "                bordercolor=COLORS['neon_green'],\n",
    "                borderwidth=2,\n",
    "                font=dict(color=COLORS['light']),\n",
    "                buttons=[\n",
    "                    dict(\n",
    "                        label='▶️ Play Animation',\n",
    "                        method='animate',\n",
    "                        args=[None, dict(\n",
    "                            frame=dict(duration=1200, redraw=True), \n",
    "                            fromcurrent=True,\n",
    "                            transition=dict(duration=400, easing='cubic-in-out')\n",
    "                        )]\n",
    "                    ),\n",
    "                    dict(\n",
    "                        label='⏸️ Pause',\n",
    "                        method='animate',\n",
    "                        args=[[None], dict(\n",
    "                            frame=dict(duration=0, redraw=False), \n",
    "                            mode='immediate'\n",
    "                        )]\n",
    "                    ),\n",
    "                    dict(\n",
    "                        label='🔄 Restart',\n",
    "                        method='animate',\n",
    "                        args=[None, dict(\n",
    "                            frame=dict(duration=1200, redraw=True), \n",
    "                            fromcurrent=False,\n",
    "                            transition=dict(duration=400, easing='cubic-in-out')\n",
    "                        )]\n",
    "                    )\n",
    "                ]\n",
    "            )\n",
    "        ],\n",
    "        \n",
    "        # Add filter label annotation\n",
    "        annotations=[\n",
    "            dict(\n",
    "                text=\"🎬 Animation Controls:\",\n",
    "                x=0.02, y=1.18,\n",
    "                xref=\"paper\", yref=\"paper\",\n",
    "                showarrow=False,\n",
    "                font=dict(size=12, family='Orbitron, monospace', color=COLORS['neon_green'])\n",
    "            )\n",
    "        ],\n",
    "        \n",
    "        # Enhanced slider with better styling\n",
    "        sliders=[\n",
    "            dict(\n",
    "                active=0,\n",
    "                yanchor='top',\n",
    "                xanchor='left',\n",
    "                currentvalue=dict(\n",
    "                    font=dict(size=16, family='Arial Black'), \n",
    "                    prefix='📅 Current Period: ', \n",
    "                    visible=True, \n",
    "                    xanchor='center'\n",
    "                ),\n",
    "                transition=dict(duration=400, easing='cubic-in-out'),\n",
    "                pad=dict(b=10, t=60),\n",
    "                len=0.85,\n",
    "                x=0.075,\n",
    "                y=-0.05,\n",
    "                bgcolor='rgba(255,255,255,0.9)',\n",
    "                bordercolor=COLORS['neutral'],\n",
    "                borderwidth=1,\n",
    "                tickcolor=COLORS['primary'],\n",
    "                steps=[\n",
    "                    dict(\n",
    "                        args=[[period], dict(\n",
    "                            frame=dict(duration=400, redraw=True), \n",
    "                            mode='immediate',\n",
    "                            transition=dict(duration=400, easing='cubic-in-out')\n",
    "                        )],\n",
    "                        label=period,\n",
    "                        method='animate',\n",
    "                        value=period\n",
    "                    ) for period in periods\n",
    "                ]\n",
    "            )\n",
    "        ]\n",
    "    )\n",
    "\n",
    "    # Add enhanced reference lines with dashboard colors\n",
    "    fig4.add_hline(\n",
    "        y=2.0, \n",
    "        line_dash=\"dot\", \n",
    "        line_color=COLORS['danger'], \n",
    "        line_width=3,\n",
    "        annotation_text=\"🎯 Pass Threshold (2.0)\",\n",
    "        annotation_position=\"top right\"\n",
    "    )\n",
    "\n",
    "    fig4.add_hline(\n",
    "        y=3.0, \n",
    "        line_dash=\"dot\", \n",
    "        line_color=COLORS['success'], \n",
    "        line_width=3,\n",
    "        annotation_text=\"🌟 Excellence Threshold (3.0)\",\n",
    "        annotation_position=\"bottom right\"\n",
    "    )\n",
    "\n",
    "    # Add subtle gradient effect with shapes using dashboard colors\n",
    "    fig4.add_shape(\n",
    "        type=\"rect\",\n",
    "        xref=\"paper\", yref=\"y\",\n",
    "        x0=0, y0=3.0, x1=1, y1=4.0,\n",
    "        fillcolor=f\"rgba({int(COLORS['success'][1:3], 16)}, {int(COLORS['success'][3:5], 16)}, {int(COLORS['success'][5:7], 16)}, 0.1)\",\n",
    "        layer=\"below\",\n",
    "        line_width=0,\n",
    "    )\n",
    "    \n",
    "    fig4.add_shape(\n",
    "        type=\"rect\",\n",
    "        xref=\"paper\", yref=\"y\",\n",
    "        x0=0, y0=2.0, x1=1, y1=3.0,\n",
    "        fillcolor=\"rgba(52, 152, 219, 0.1)\",\n",
    "        layer=\"below\",\n",
    "        line_width=0,\n",
    "    )\n",
    "    \n",
    "    fig4.add_shape(\n",
    "        type=\"rect\",\n",
    "        xref=\"paper\", yref=\"y\",\n",
    "        x0=0, y0=1.5, x1=1, y1=2.0,\n",
    "        fillcolor=\"rgba(231, 76, 60, 0.1)\",\n",
    "        layer=\"below\",\n",
    "        line_width=0,\n",
    "    )\n",
    "\n",
    "    fig4.show()\n",
    "    print(\"✅ Chart 4 completed!\")\n",
    "else:\n",
    "    print(\"⚠️ No sufficient data for GPA trends animation\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "870eb255",
   "metadata": {},
   "source": [
    "# PART 3: ANALYTICS INSIGHTS & DASHBOARD INTEGRATION\n",
    "## Summary Statistics and Actionable Insights\n",
    "\n",
    "This section provides comprehensive insights from the data analysis and prepares the foundation for dashboard integration."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "6879e669",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "============================================================\n",
      "📊 COMPREHENSIVE ANALYTICS INSIGHTS\n",
      "============================================================\n",
      "\n",
      "🎯 GPA vs COMPLETION TIME INSIGHTS:\n",
      "==================================================\n",
      "📊 SUCCESS SCORE DISTRIBUTION:\n",
      "   • Top 25%: Success Score ≥ 89.2\n",
      "   • Median: 84.0\n",
      "   • Bottom 25%: Success Score ≤ 80.0\n",
      "\n",
      "🚨 RISK ASSESSMENT BREAKDOWN:\n",
      "   • Low Risk: 40 students (71.4%) - Avg: 3.25 GPA, 5.9 months\n",
      "   • Medium Risk: 16 students (28.6%) - Avg: 2.94 GPA, 17.0 months\n",
      "   • High Risk: 0 students (0.0%) - Avg: nan GPA, nan months\n",
      "\n",
      "⏰ COMPLETION TIME vs GPA ANALYSIS:\n",
      "   • Fast completion (≤30 months): 56 students, Avg GPA: 3.16\n",
      "   • Slow completion (>48 months): 0 students, Avg GPA: nan\n",
      "\n",
      "🎯 HIGH PERFORMERS vs LOW PERFORMERS:\n",
      "   • Elite High Achievers (GPA > 3.5 & < 5 months): 5 students\n",
      "   • Low GPA (<2.0): 0 students, Avg completion: nan months\n",
      "\n",
      "🎯 KEY RECOMMENDATIONS:\n",
      "   • 5 students are elite high achievers (GPA > 3.5 + completion < 5 months)\n",
      "   • 0 students are struggling (low GPA + slow completion)\n",
      "✅ Detailed insights analysis completed!\n"
     ]
    }
   ],
   "source": [
    "# === COMPREHENSIVE ANALYTICS INSIGHTS ===\n",
    "print(\"\\n\" + \"=\"*60)\n",
    "print(\"📊 COMPREHENSIVE ANALYTICS INSIGHTS\")\n",
    "print(\"=\"*60)\n",
    "\n",
    "# Analyze and print insights focusing on GPA vs Completion Time\n",
    "print(\"\\n🎯 GPA vs COMPLETION TIME INSIGHTS:\")\n",
    "print(\"=\" * 50)\n",
    "\n",
    "print(\"📊 SUCCESS SCORE DISTRIBUTION:\")\n",
    "success_quartiles = scatter_data['SUCCESS_SCORE'].quantile([0.25, 0.5, 0.75])\n",
    "print(f\"   • Top 25%: Success Score ≥ {success_quartiles[0.75]:.1f}\")\n",
    "print(f\"   • Median: {success_quartiles[0.5]:.1f}\")\n",
    "print(f\"   • Bottom 25%: Success Score ≤ {success_quartiles[0.25]:.1f}\")\n",
    "\n",
    "print(f\"\\n🚨 RISK ASSESSMENT BREAKDOWN:\")\n",
    "risk_breakdown = scatter_data['RISK_CATEGORY'].value_counts()\n",
    "for risk, count in risk_breakdown.items():\n",
    "    percentage = (count / len(scatter_data)) * 100\n",
    "    avg_completion = scatter_data[scatter_data['RISK_CATEGORY'] == risk]['COMPLETION_MONTHS'].mean()\n",
    "    avg_gpa = scatter_data[scatter_data['RISK_CATEGORY'] == risk]['CUMULATIVE_GPA'].mean()\n",
    "    print(f\"   • {risk}: {count} students ({percentage:.1f}%) - Avg: {avg_gpa:.2f} GPA, {avg_completion:.1f} months\")\n",
    "\n",
    "print(f\"\\n⏰ COMPLETION TIME vs GPA ANALYSIS:\")\n",
    "fast_students = scatter_data[scatter_data['COMPLETION_MONTHS'] <= 30]\n",
    "slow_students = scatter_data[scatter_data['COMPLETION_MONTHS'] > 48]\n",
    "print(f\"   • Fast completion (≤30 months): {len(fast_students)} students, Avg GPA: {fast_students['CUMULATIVE_GPA'].mean():.2f}\")\n",
    "print(f\"   • Slow completion (>48 months): {len(slow_students)} students, Avg GPA: {slow_students['CUMULATIVE_GPA'].mean():.2f}\")\n",
    "\n",
    "print(f\"\\n🎯 HIGH PERFORMERS vs LOW PERFORMERS:\")\n",
    "high_gpa = scatter_data[(scatter_data['CUMULATIVE_GPA'] > 3.5) & (scatter_data['COMPLETION_MONTHS'] < 5)]\n",
    "low_gpa = scatter_data[scatter_data['CUMULATIVE_GPA'] < 2.0]\n",
    "print(f\"   • Elite High Achievers (GPA > 3.5 & < 5 months): {len(high_gpa)} students\")\n",
    "print(f\"   • Low GPA (<2.0): {len(low_gpa)} students, Avg completion: {low_gpa['COMPLETION_MONTHS'].mean():.1f} months\")\n",
    "\n",
    "print(f\"\\n🎯 KEY RECOMMENDATIONS:\")\n",
    "high_risk_students = scatter_data[scatter_data['RISK_CATEGORY'] == 'High Risk']\n",
    "if len(high_risk_students) > 0:\n",
    "    print(f\"   • {len(high_risk_students)} students need immediate academic support\")\n",
    "    \n",
    "fast_excellent = scatter_data[(scatter_data['COMPLETION_MONTHS'] < 5) & (scatter_data['CUMULATIVE_GPA'] > 3.5)]\n",
    "if len(fast_excellent) > 0:\n",
    "    print(f\"   • {len(fast_excellent)} students are elite high achievers (GPA > 3.5 + completion < 5 months)\")\n",
    "    \n",
    "at_risk = scatter_data[(scatter_data['CUMULATIVE_GPA'] < 2.5) & (scatter_data['COMPLETION_MONTHS'] > 42)]\n",
    "print(f\"   • {len(at_risk)} students are struggling (low GPA + slow completion)\")\n",
    "\n",
    "print(\"✅ Detailed insights analysis completed!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "d24a9abf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "============================================================\n",
      "📊 KEY METRICS SUMMARY FOR DASHBOARD\n",
      "============================================================\n",
      "📈 Total Students Analyzed: 285\n",
      "⏱️ Average Completion Time: 9.5 months\n",
      "🎯 Overall Average GPA: 3.16\n",
      "✅ Pass Rate (GPA ≥ 2.0): 95.4%\n",
      "🏆 Top Performing Citizenship: FOREIGNER\n",
      "💰 Best Funding Type: Individual - SFC + $1000 SCHOLARSHIP\n",
      "⚡ Fastest Completion Group: SG PR\n",
      "📚 Analysis covers enrollment and completion patterns\n",
      "\n",
      "🎨 VISUALIZATION SYSTEM COMPLETED!\n",
      "Each chart features:\n",
      "• Chart 1: Population distribution treemap\n",
      "• Chart 2: Interactive GPA vs completion time correlation analysis\n",
      "• Chart 3: Course completion time distribution patterns\n",
      "• Chart 4: Animated GPA trends over semesters\n",
      "• Interactive elements (dropdowns, sliders, play/pause)\n",
      "• Comprehensive hover information\n",
      "• Actionable insights for decision-making\n",
      "\n",
      "🔗 DATA PREPARATION STATUS:\n",
      "• ✅ All datasets loaded and processed\n",
      "• ✅ Advanced calculated fields generated\n",
      "• ✅ Risk assessment scoring completed\n",
      "• ✅ Success prediction metrics calculated\n",
      "• ✅ Interactive visualizations created\n",
      "• ✅ Template aesthetic consistency maintained\n",
      "• ✅ Ready for dashboard integration\n",
      "\n",
      "📊 DASHBOARD INTEGRATION READY!\n",
      "This analysis system can now be integrated with:\n",
      "• Dash web application framework\n",
      "• Real-time filtering capabilities\n",
      "• Student search functionality\n",
      "• KPI monitoring dashboards\n",
      "• Administrative decision support tools\n"
     ]
    }
   ],
   "source": [
    "# === SUMMARY STATISTICS FOR DASHBOARD INTEGRATION ===\n",
    "print(\"\\n\" + \"=\"*60)\n",
    "print(\"📊 KEY METRICS SUMMARY FOR DASHBOARD\")\n",
    "print(\"=\"*60)\n",
    "\n",
    "# Calculate key metrics\n",
    "total_students = len(df)\n",
    "avg_completion_time = df['COMPLETION_MONTHS'].mean()\n",
    "avg_gpa = df['CUMULATIVE_GPA'].mean()\n",
    "pass_rate = (df['ACADEMIC_OUTCOME'] == 'Pass').mean() * 100\n",
    "best_citizenship = df.groupby('CITIZENSHIP')['CUMULATIVE_GPA'].mean().idxmax()\n",
    "best_funding = df.groupby('COURSE FUNDING')['CUMULATIVE_GPA'].mean().idxmax()\n",
    "fastest_completion = df.groupby('CITIZENSHIP')['COMPLETION_MONTHS'].mean().idxmin()\n",
    "\n",
    "print(f\"📈 Total Students Analyzed: {total_students:,}\")\n",
    "print(f\"⏱️ Average Completion Time: {avg_completion_time:.1f} months\")\n",
    "print(f\"🎯 Overall Average GPA: {avg_gpa:.2f}\")\n",
    "print(f\"✅ Pass Rate (GPA ≥ 2.0): {pass_rate:.1f}%\")\n",
    "print(f\"🏆 Top Performing Citizenship: {best_citizenship}\")\n",
    "print(f\"💰 Best Funding Type: {best_funding}\")\n",
    "print(f\"⚡ Fastest Completion Group: {fastest_completion}\")\n",
    "print(f\"📚 Analysis covers enrollment and completion patterns\")\n",
    "\n",
    "print(\"\\n🎨 VISUALIZATION SYSTEM COMPLETED!\")\n",
    "print(\"Each chart features:\")\n",
    "print(\"• Chart 1: Population distribution treemap\")\n",
    "print(\"• Chart 2: Interactive GPA vs completion time correlation analysis\")\n",
    "print(\"• Chart 3: Course completion time distribution patterns\")\n",
    "print(\"• Chart 4: Animated GPA trends over semesters\")\n",
    "print(\"• Interactive elements (dropdowns, sliders, play/pause)\")\n",
    "print(\"• Comprehensive hover information\")\n",
    "print(\"• Actionable insights for decision-making\")\n",
    "\n",
    "print(f\"\\n🔗 DATA PREPARATION STATUS:\")\n",
    "print(\"• ✅ All datasets loaded and processed\")\n",
    "print(\"• ✅ Advanced calculated fields generated\")\n",
    "print(\"• ✅ Risk assessment scoring completed\")\n",
    "print(\"• ✅ Success prediction metrics calculated\")\n",
    "print(\"• ✅ Interactive visualizations created\")\n",
    "print(\"• ✅ Template aesthetic consistency maintained\")\n",
    "print(\"• ✅ Ready for dashboard integration\")\n",
    "\n",
    "print(f\"\\n📊 DASHBOARD INTEGRATION READY!\")\n",
    "print(\"This analysis system can now be integrated with:\")\n",
    "print(\"• Dash web application framework\")\n",
    "print(\"• Real-time filtering capabilities\")\n",
    "print(\"• Student search functionality\")\n",
    "print(\"• KPI monitoring dashboards\")\n",
    "print(\"• Administrative decision support tools\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d517e1a0",
   "metadata": {},
   "source": [
    "# PART 4: INTERACTIVE DASHBOARD IMPLEMENTATION\n",
    "## Futuristic Analytics Dashboard with Dash Framework\n",
    "\n",
    "This section integrates all the analysis and charts into a live, interactive web dashboard with search functionality and real-time KPI monitoring."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "1998f506",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "🚀 Initializing Futuristic Analytics Dashboard...\n",
      "✅ Dashboard framework initialized with date picker overlay fix!\n"
     ]
    }
   ],
   "source": [
    "# === DASHBOARD APP INITIALIZATION (MATCHING TEMPLATE) ===\n",
    "print(\"🚀 Initializing Futuristic Analytics Dashboard...\")\n",
    "\n",
    "# Import Dash framework\n",
    "from dash import Dash, html, dcc, Input, Output, State, callback\n",
    "import dash_bootstrap_components as dbc\n",
    "from datetime import datetime, timedelta\n",
    "\n",
    "# ================================\n",
    "# APP INITIALIZATION WITH DATE PICKER FIX\n",
    "# ================================\n",
    "app = Dash(\n",
    "    __name__,\n",
    "    external_stylesheets=[\n",
    "        dbc.themes.CYBORG,  # Futuristic dark theme\n",
    "        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css'\n",
    "    ],\n",
    "    suppress_callback_exceptions=True\n",
    ")\n",
    "\n",
    "app.title = \"Student Analytics Dashboard\"\n",
    "\n",
    "# Custom CSS to fix date picker z-index overlay issues\n",
    "app.index_string = '''\n",
    "<!DOCTYPE html>\n",
    "<html>\n",
    "    <head>\n",
    "        {%metas%}\n",
    "        <title>{%title%}</title>\n",
    "        {%favicon%}\n",
    "        {%css%}\n",
    "        <style>\n",
    "            .DateInput_input, .DateRangePickerInput {\n",
    "                z-index: 9999 !important;\n",
    "                position: relative !important;\n",
    "            }\n",
    "            .DateRangePicker, .DayPicker {\n",
    "                z-index: 10000 !important;\n",
    "                position: absolute !important;\n",
    "            }\n",
    "            .SingleDatePicker_picker {\n",
    "                z-index: 10004 !important;\n",
    "                position: absolute !important;\n",
    "            }\n",
    "            .SingleDatePickerInput {\n",
    "                z-index: 10006 !important;\n",
    "                position: relative !important;\n",
    "            }\n",
    "            .DayPicker_portal {\n",
    "                z-index: 10002 !important;\n",
    "            }\n",
    "            .DateInput_fang {\n",
    "                z-index: 10003 !important;\n",
    "            }\n",
    "        </style>\n",
    "    </head>\n",
    "    <body>\n",
    "        {%app_entry%}\n",
    "        <footer>\n",
    "            {%config%}\n",
    "            {%scripts%}\n",
    "            {%renderer%}\n",
    "        </footer>\n",
    "    </body>\n",
    "</html>\n",
    "'''\n",
    "\n",
    "print(\"✅ Dashboard framework initialized with date picker overlay fix!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "68d410b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "🎨 Creating futuristic header component...\n",
      "✅ Header component created!\n"
     ]
    }
   ],
   "source": [
    "# === DASHBOARD HEADER COMPONENT (MATCHING TEMPLATE) ===\n",
    "print(\"🎨 Creating futuristic header component...\")\n",
    "\n",
    "# Header with enhanced glowing effects - EXACT TEMPLATE MATCH\n",
    "header = dbc.Container([\n",
    "    dbc.Row([\n",
    "        dbc.Col([\n",
    "            html.Div([\n",
    "                html.Div([\n",
    "                    html.I(className=\"fas fa-graduation-cap\", \n",
    "                          style={\n",
    "                              'fontSize': '1.8rem', \n",
    "                              'color': COLORS['neon_blue'],\n",
    "                              'filter': 'drop-shadow(0 0 8px rgba(0, 245, 255, 0.8))'\n",
    "                          }),\n",
    "                ], style={\n",
    "                    'width': '50px', 'height': '50px', 'borderRadius': '15px',\n",
    "                    'background': f'linear-gradient(135deg, {COLORS[\"primary\"]} 0%, {COLORS[\"neon_blue\"]} 100%)',\n",
    "                    'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center',\n",
    "                    'marginRight': '15px', \n",
    "                    'boxShadow': f'0 0 25px {COLORS[\"glow_shadow\"]}, 0 0 50px rgba(139, 95, 191, 0.3)',\n",
    "                    'border': f'1px solid {COLORS[\"neon_blue\"]}',\n",
    "                    'animation': 'pulse 2s infinite'\n",
    "                }),\n",
    "                html.Div([\n",
    "                    html.H5(\"STUDENT ANALYTICS\", style={\n",
    "                        'color': COLORS['light'], 'margin': '0', 'fontWeight': '700',\n",
    "                        'letterSpacing': '1px', 'fontSize': '0.95rem',\n",
    "                        'textShadow': f'0 0 10px {COLORS[\"neon_blue\"]}',\n",
    "                        'fontFamily': 'Orbitron, monospace'\n",
    "                    }),\n",
    "                    html.P(\"CONTROL CENTER\", style={\n",
    "                        'color': COLORS['neon_blue'], 'margin': '0', 'fontSize': '0.75rem',\n",
    "                        'fontWeight': '500', 'letterSpacing': '0.5px',\n",
    "                        'fontFamily': 'Rajdhani, monospace'\n",
    "                    })\n",
    "                ])\n",
    "            ], style={'display': 'flex', 'alignItems': 'center'})\n",
    "        ], width=3),\n",
    "        \n",
    "        dbc.Col([\n",
    "            html.H1(\"ANALYTICS NEXUS\", \n",
    "                   className=\"text-center\",\n",
    "                   style={\n",
    "                       'color': COLORS['light'], \n",
    "                       'fontWeight': '900',\n",
    "                       'fontSize': '2.5rem',\n",
    "                       'margin': '0',\n",
    "                       'background': f'linear-gradient(135deg, {COLORS[\"neon_blue\"]} 0%, {COLORS[\"neon_purple\"]} 50%, {COLORS[\"primary\"]} 100%)',\n",
    "                       'backgroundClip': 'text',\n",
    "                       'WebkitBackgroundClip': 'text',\n",
    "                       'WebkitTextFillColor': 'transparent',\n",
    "                       'letterSpacing': '2px',\n",
    "                       'textShadow': '0 0 20px rgba(34, 211, 238, 0.6)',\n",
    "                       'filter': 'drop-shadow(0 0 10px rgba(34, 211, 238, 0.8))',\n",
    "                       'fontFamily': 'Orbitron, monospace'\n",
    "                   })\n",
    "        ], width=6),\n",
    "        \n",
    "        dbc.Col([\n",
    "            html.Div([\n",
    "                html.Div([\n",
    "                    html.Div([\n",
    "                        html.I(className=\"fas fa-circle\", style={\n",
    "                            'color': COLORS['neon_green'], 'fontSize': '0.6rem',\n",
    "                            'animation': 'blink 1.5s infinite'\n",
    "                        }),\n",
    "                        html.Span(\"LIVE\", style={\n",
    "                            'color': COLORS['neon_green'], 'fontSize': '0.8rem', \n",
    "                            'marginLeft': '6px', 'fontWeight': '700',\n",
    "                            'textShadow': f'0 0 8px {COLORS[\"neon_green\"]}',\n",
    "                            'fontFamily': 'Orbitron, monospace'\n",
    "                        })\n",
    "                    ], style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '4px'}),\n",
    "                    html.Span(id=\"live-time\", style={\n",
    "                        'color': COLORS['text'], 'fontSize': '0.85rem',\n",
    "                        'fontFamily': 'Rajdhani, monospace', 'fontWeight': '500'\n",
    "                    })\n",
    "                ], style={'textAlign': 'right'})\n",
    "            ])\n",
    "        ], width=3)\n",
    "    ], className=\"align-items-center\"),\n",
    "], fluid=True, className=\"py-4\", \n",
    "   style={\n",
    "       'background': f'linear-gradient(135deg, {COLORS[\"card_bg\"]} 0%, {COLORS[\"sidebar_bg\"]} 100%)', \n",
    "       'marginBottom': '30px',\n",
    "       'borderRadius': '0 0 30px 30px',\n",
    "       'boxShadow': f'0 0 40px {COLORS[\"glow_shadow\"]}, 0 0 50px rgba(26, 26, 46, 0.8)',\n",
    "       'border': f'1px solid {COLORS[\"neon_blue\"]}20',\n",
    "       'position': 'relative',\n",
    "       'overflow': 'hidden'\n",
    "   })\n",
    "\n",
    "print(\"✅ Header component created!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "f12ba544",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "🎨 Creating main layout to match template...\n"
     ]
    }
   ],
   "source": [
    "# === MAIN LAYOUT (EXACT TEMPLATE MATCH) ===\n",
    "print(\"🎨 Creating main layout to match template...\")\n",
    "\n",
    "# Chart containers with enhanced glowing design (matching template)\n",
    "chart_style = {\n",
    "    'background': f'linear-gradient(135deg, {COLORS[\"card_bg\"]} 0%, {COLORS[\"sidebar_bg\"]} 100%)',\n",
    "    'border': f'2px solid {COLORS[\"neon_blue\"]}40',\n",
    "    'borderRadius': '25px',\n",
    "    'padding': '30px',\n",
    "    'marginBottom': '30px',\n",
    "    'boxShadow': f'0 0 40px {COLORS[\"glow_shadow\"]}, 0 15px 60px rgba(26, 26, 46, 0.8)',\n",
    "    'backdropFilter': 'blur(15px)',\n",
    "    'position': 'relative',\n",
    "    'zIndex': '1',\n",
    "    'overflow': 'hidden',\n",
    "    'transition': 'all 0.3s ease'\n",
    "}\n",
    "\n",
    "# ================================\n",
    "# MAIN LAYOUT WITH LEFT-RIGHT ORIENTATION (EXACT TEMPLATE MATCH)\n",
    "# ================================\n",
    "app.layout = html.Div([\n",
    "    # Global CSS for futuristic fonts and date picker fix\n",
    "    html.Link(\n",
    "        rel='stylesheet',\n",
    "        href='https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap'\n",
    "    ),\n",
    "    \n",
    "    # Live update interval\n",
    "    dcc.Interval(id='interval-update', interval=60000, n_intervals=0),\n",
    "    \n",
    "    # Data store\n",
    "    dcc.Store(id='filtered-data'),\n",
    "    \n",
    "    # Header (full width)\n",
    "    header,\n",
    "    \n",
    "    # Main Content Container with Left-Right Layout\n",
    "    dbc.Container([\n",
    "        dbc.Row([\n",
    "            # LEFT SIDE - Search, Student Data, and KPIs (4/12 columns)\n",
    "            dbc.Col([\n",
    "                # Search Section\n",
    "                html.Div([\n",
    "                    html.Label(\"🔍 SEARCH STUDENT ID\", style={\n",
    "                        'color': COLORS['pink'], 'fontWeight': '700', 'marginBottom': '15px',\n",
    "                        'fontSize': '1rem', 'letterSpacing': '1px',\n",
    "                        'textShadow': f'0 0 8px {COLORS[\"pink\"]}',\n",
    "                        'fontFamily': 'Orbitron, monospace'\n",
    "                    }),\n",
    "                    dbc.Input(\n",
    "                        id='search-box',\n",
    "                        placeholder=\"Enter Student ID (e.g., STU00001)\",\n",
    "                        type=\"text\",\n",
    "                        style={\n",
    "                            'backgroundColor': COLORS['sidebar_bg'], 'color': COLORS['light'], \n",
    "                            'border': f'2px solid {COLORS[\"pink\"]}60', 'borderRadius': '10px',\n",
    "                            'boxShadow': f'inset 0 0 10px rgba(236, 72, 153, 0.2)',\n",
    "                            'fontFamily': 'Rajdhani, monospace',\n",
    "                            'fontSize': '1rem'\n",
    "                        }\n",
    "                    )\n",
    "                ], style={\n",
    "                    'backgroundColor': COLORS['card_bg'], 'padding': '20px', 'borderRadius': '20px',\n",
    "                    'boxShadow': f'0 0 30px rgba(236, 72, 153, 0.4), 0 8px 32px rgba(26, 26, 46, 0.6)', \n",
    "                    'border': f'2px solid {COLORS[\"pink\"]}40',\n",
    "                    'backdropFilter': 'blur(10px)',\n",
    "                    'marginBottom': '20px'\n",
    "                }),\n",
    "                \n",
    "                # Student Data Section\n",
    "                html.Div([\n",
    "                    html.H4(\"📊 STUDENT DATA\", \n",
    "                           style={\n",
    "                               'color': COLORS['neon_green'], 'textAlign': 'center', 'marginBottom': '20px',\n",
    "                               'fontWeight': '900', 'fontSize': '1.1rem', 'letterSpacing': '2px',\n",
    "                               'fontFamily': 'Orbitron, monospace',\n",
    "                               'textShadow': f'0 0 15px {COLORS[\"neon_green\"]}, 0 0 30px {COLORS[\"neon_green\"]}40',\n",
    "                               'textTransform': 'uppercase'\n",
    "                           }),\n",
    "                    html.Div(id='student-data-table')\n",
    "                ], style={**chart_style, 'height': '300px', 'overflow': 'auto', 'marginBottom': '20px'}),\n",
    "                \n",
    "                # KPI Cards Section (Compact vertical layout)\n",
    "                html.Div([\n",
    "                    html.H4(\"📈 KEY METRICS\", \n",
    "                           style={\n",
    "                               'color': COLORS['neon_blue'], 'textAlign': 'center', 'marginBottom': '20px',\n",
    "                               'fontWeight': '900', 'fontSize': '1.1rem', 'letterSpacing': '2px',\n",
    "                               'fontFamily': 'Orbitron, monospace',\n",
    "                               'textShadow': f'0 0 15px {COLORS[\"neon_blue\"]}, 0 0 30px {COLORS[\"neon_blue\"]}40',\n",
    "                               'textTransform': 'uppercase'\n",
    "                           }),\n",
    "                    html.Div(id='kpi-cards-left')\n",
    "                ], style=chart_style)\n",
    "                \n",
    "            ], width=4),  # Left side takes 4/12 columns\n",
    "            \n",
    "            # RIGHT SIDE - Scrollable Charts (8/12 columns)\n",
    "            dbc.Col([\n",
    "                # Simple Date Filter Row with Fixed Z-Index\n",
    "                html.Div([\n",
    "                    html.Span(\"📅 Filter: \", style={\n",
    "                        'color': COLORS['secondary'], 'fontWeight': '700', 'marginRight': '10px',\n",
    "                        'fontFamily': 'Orbitron, monospace', 'fontSize': '0.9rem'\n",
    "                    }),\n",
    "                    html.Div([\n",
    "                        dcc.DatePickerSingle(\n",
    "                            id='start-date-picker',\n",
    "                            date=datetime(2022, 4, 1),  # Start of actual data range\n",
    "                            display_format='YYYY-MM-DD',\n",
    "                            style={\n",
    "                                'display': 'inline-block', \n",
    "                                'marginRight': '10px',\n",
    "                                'zIndex': '9999'  # High z-index for calendar dropdown\n",
    "                            }\n",
    "                        )\n",
    "                    ], style={\n",
    "                        'display': 'inline-block', \n",
    "                        'position': 'relative',\n",
    "                        'zIndex': '9999'  # Container z-index\n",
    "                    }),\n",
    "                    html.Span(\" to \", style={'color': COLORS['light'], 'margin': '0 5px'}),\n",
    "                    html.Div([\n",
    "                        dcc.DatePickerSingle(\n",
    "                            id='end-date-picker',\n",
    "                            date=datetime(2025, 4, 24),  # End of actual data range\n",
    "                            display_format='YYYY-MM-DD',\n",
    "                            style={\n",
    "                                'display': 'inline-block', \n",
    "                                'marginRight': '15px',\n",
    "                                'zIndex': '9999'  # High z-index for calendar dropdown\n",
    "                            }\n",
    "                        )\n",
    "                    ], style={\n",
    "                        'display': 'inline-block', \n",
    "                        'position': 'relative',\n",
    "                        'zIndex': '9999'  # Container z-index\n",
    "                    }),\n",
    "                    dbc.Button(\"All Time\", id=\"btn-all-years\", color=\"outline-info\", size=\"sm\",\n",
    "                              style={'fontFamily': 'Rajdhani, monospace', 'fontSize': '0.8rem'})\n",
    "                ], style={\n",
    "                    'backgroundColor': COLORS['card_bg'], \n",
    "                    'padding': '10px 15px', \n",
    "                    'borderRadius': '10px',\n",
    "                    'border': f'1px solid {COLORS[\"secondary\"]}40', \n",
    "                    'marginBottom': '15px',\n",
    "                    'display': 'flex', \n",
    "                    'alignItems': 'center', \n",
    "                    'flexWrap': 'wrap',\n",
    "                    'position': 'relative',\n",
    "                    'zIndex': '1000'  # Base z-index for filter container\n",
    "                }),\n",
    "                \n",
    "                # Scrollable Charts Container\n",
    "                html.Div([\n",
    "                    # Chart 1 - Your Treemap\n",
    "                    html.Div([\n",
    "                        html.H4(\"POPULATION DISTRIBUTION\", \n",
    "                               style={\n",
    "                                   'color': COLORS['neon_blue'], 'textAlign': 'center', 'marginBottom': '20px',\n",
    "                                   'fontWeight': '900', 'fontSize': '1.4rem', 'letterSpacing': '2px',\n",
    "                                   'fontFamily': 'Orbitron, monospace',\n",
    "                                   'textShadow': f'0 0 15px {COLORS[\"neon_blue\"]}, 0 0 30px {COLORS[\"neon_blue\"]}40',\n",
    "                                   'textTransform': 'uppercase'\n",
    "                               }),\n",
    "                        dcc.Graph(id='chart-1', \n",
    "                                 config={'displayModeBar': True, 'displaylogo': False},\n",
    "                                 style={'height': '800px'})\n",
    "                    ], style={**chart_style, 'marginBottom': '40px'}),\n",
    "                    \n",
    "                    # Chart 2 - Your Scatter\n",
    "                    html.Div([\n",
    "                        html.H4(\"GPA vs COMPLETION ANALYSIS\", \n",
    "                               style={\n",
    "                                   'color': COLORS['neon_purple'], 'textAlign': 'center', 'marginBottom': '20px',\n",
    "                                   'fontWeight': '900', 'fontSize': '1.4rem', 'letterSpacing': '2px',\n",
    "                                   'fontFamily': 'Orbitron, monospace',\n",
    "                                   'textShadow': f'0 0 15px {COLORS[\"neon_purple\"]}, 0 0 30px {COLORS[\"neon_purple\"]}40',\n",
    "                                   'textTransform': 'uppercase'\n",
    "                               }),\n",
    "                        dcc.Graph(id='chart-2', \n",
    "                                 config={'displayModeBar': True, 'displaylogo': False},\n",
    "                                 style={'height': '800px'})\n",
    "                    ], style={**chart_style, 'marginBottom': '40px'}),\n",
    "                    \n",
    "                    # Chart 3 - Your Boxplot\n",
    "                    html.Div([\n",
    "                        html.H4(\"COMPLETION TIME ANALYSIS\", \n",
    "                               style={\n",
    "                                   'color': COLORS['neon_green'], 'textAlign': 'center', 'marginBottom': '20px',\n",
    "                                   'fontWeight': '900', 'fontSize': '1.4rem', 'letterSpacing': '2px',\n",
    "                                   'fontFamily': 'Orbitron, monospace',\n",
    "                                   'textShadow': f'0 0 15px {COLORS[\"neon_green\"]}, 0 0 30px {COLORS[\"neon_green\"]}40',\n",
    "                                   'textTransform': 'uppercase'\n",
    "                               }),\n",
    "                        dcc.Graph(id='chart-3', \n",
    "                                 config={'displayModeBar': True, 'displaylogo': False},\n",
    "                                 style={'height': '800px'})\n",
    "                    ], style={**chart_style, 'marginBottom': '40px'}),\n",
    "                    \n",
    "                    # Chart 4 - Your Animation\n",
    "                    html.Div([\n",
    "                        html.H4(\"TEMPORAL TRENDS\", \n",
    "                               style={\n",
    "                                   'color': COLORS['accent'], 'textAlign': 'center', 'marginBottom': '20px',\n",
    "                                   'fontWeight': '900', 'fontSize': '1.4rem', 'letterSpacing': '2px',\n",
    "                                   'fontFamily': 'Orbitron, monospace',\n",
    "                                   'textShadow': f'0 0 15px {COLORS[\"accent\"]}, 0 0 30px {COLORS[\"accent\"]}40',\n",
    "                                   'textTransform': 'uppercase'\n",
    "                               }),\n",
    "                        dcc.Graph(id='chart-4', \n",
    "                                 config={'displayModeBar': True, 'displaylogo': False},\n",
    "                                 style={'height': '800px'})\n",
    "                    ], style=chart_style)\n",
    "                    \n",
    "                ], style={\n",
    "                    'height': '90vh',  # Set viewport height\n",
    "                    'overflowY': 'auto',  # Enable vertical scrolling\n",
    "                    'paddingRight': '15px',  # Space for scrollbar\n",
    "                    'scrollbarWidth': 'thin',  # Thin scrollbar for Firefox\n",
    "                    'scrollbarColor': f'{COLORS[\"neon_blue\"]} {COLORS[\"sidebar_bg\"]}'  # Custom scrollbar colors\n",
    "                })\n",
    "                \n",
    "            ], width=8)  # Right side takes 8/12 columns\n",
    "            \n",
    "        ], className=\"g-4\")\n",
    "    ], fluid=True)\n",
    "], style={\n",
    "    'backgroundColor': COLORS['dark_bg'], \n",
    "    'minHeight': '100vh', \n",
    "    'padding': '0',\n",
    "    'fontFamily': 'Rajdhani, Orbitron, monospace'\n",
    "})\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "4b5b2683",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "🔗 Creating callbacks to match template with your actual data...\n",
      "✅ All callbacks configured with your actual data structure!\n",
      "📊 Dashboard ready for 285 students with real metrics!\n",
      "🔄 Charts will now show EMPTY when no data matches filters!\n",
      "⏰ 'All Time' button will reset date range automatically!\n"
     ]
    }
   ],
   "source": [
    "# === DASHBOARD CALLBACKS (MATCHING TEMPLATE PATTERN) ===\n",
    "print(\"🔗 Creating callbacks to match template with your actual data...\")\n",
    "\n",
    "# Main callback to update student data, KPIs, and filtered data\n",
    "@app.callback(\n",
    "    [Output('student-data-table', 'children'),\n",
    "     Output('kpi-cards-left', 'children'),\n",
    "     Output('filtered-data', 'data')],\n",
    "    [Input('search-box', 'value'),\n",
    "     Input('start-date-picker', 'date'),\n",
    "     Input('end-date-picker', 'date'),\n",
    "     Input('btn-all-years', 'n_clicks')]\n",
    ")\n",
    "def update_dashboard(search_value, start_date, end_date, btn_clicks):\n",
    "    from dash import callback_context\n",
    "    \n",
    "    # Start with full dataset (your actual data)\n",
    "    filtered_df = df.copy()\n",
    "    \n",
    "    # Handle \"All Time\" button\n",
    "    if callback_context.triggered and 'btn-all-years' in callback_context.triggered[0]['prop_id']:\n",
    "        start_date = None\n",
    "        end_date = None\n",
    "    \n",
    "    # Apply ONLY date filters for charts and KPIs (NOT search filter)\n",
    "    chart_filtered_df = filtered_df.copy()\n",
    "    if start_date and 'COMMENCEMENT DATE' in chart_filtered_df.columns:\n",
    "        chart_filtered_df = chart_filtered_df[pd.to_datetime(chart_filtered_df['COMMENCEMENT DATE']) >= pd.to_datetime(start_date)]\n",
    "    if end_date and 'COMMENCEMENT DATE' in chart_filtered_df.columns:\n",
    "        chart_filtered_df = chart_filtered_df[pd.to_datetime(chart_filtered_df['COMMENCEMENT DATE']) <= pd.to_datetime(end_date)]\n",
    "    \n",
    "    # Calculate KPIs from date-filtered data only\n",
    "    total_students = len(chart_filtered_df)\n",
    "    avg_gpa = chart_filtered_df['CUMULATIVE_GPA'].mean() if len(chart_filtered_df) > 0 and 'CUMULATIVE_GPA' in chart_filtered_df.columns else 0\n",
    "    avg_completion = chart_filtered_df['COMPLETION_MONTHS'].mean() if len(chart_filtered_df) > 0 and 'COMPLETION_MONTHS' in chart_filtered_df.columns else 0\n",
    "    \n",
    "    # Pass rate calculation (assuming GPA >= 2.0 is pass)\n",
    "    if len(chart_filtered_df) > 0 and 'CUMULATIVE_GPA' in chart_filtered_df.columns:\n",
    "        pass_rate = (chart_filtered_df['CUMULATIVE_GPA'] >= 2.0).mean() * 100\n",
    "    else:\n",
    "        pass_rate = 0\n",
    "    \n",
    "    # Create KPI display (template style with your metrics)\n",
    "    kpi_display = html.Div([\n",
    "        html.Div([\n",
    "            html.H3(f\"{total_students:,}\", style={\n",
    "                'color': COLORS['neon_blue'], 'fontWeight': '900', 'margin': '0',\n",
    "                'fontFamily': 'Orbitron, monospace', 'fontSize': '2rem'\n",
    "            }),\n",
    "            html.P(\"Total Students\", style={\n",
    "                'color': COLORS['text'], 'margin': '5px 0 15px 0', 'fontSize': '0.9rem',\n",
    "                'fontFamily': 'Rajdhani, monospace'\n",
    "            })\n",
    "        ]),\n",
    "        html.Div([\n",
    "            html.H3(f\"{avg_gpa:.2f}\" if avg_gpa > 0 else \"N/A\", style={\n",
    "                'color': COLORS['neon_green'], 'fontWeight': '900', 'margin': '0',\n",
    "                'fontFamily': 'Orbitron, monospace', 'fontSize': '2rem'\n",
    "            }),\n",
    "            html.P(\"Average GPA\", style={\n",
    "                'color': COLORS['text'], 'margin': '5px 0 15px 0', 'fontSize': '0.9rem',\n",
    "                'fontFamily': 'Rajdhani, monospace'\n",
    "            })\n",
    "        ]),\n",
    "        html.Div([\n",
    "            html.H3(f\"{avg_completion:.1f}\" if avg_completion > 0 else \"N/A\", style={\n",
    "                'color': COLORS['accent'], 'fontWeight': '900', 'margin': '0',\n",
    "                'fontFamily': 'Orbitron, monospace', 'fontSize': '2rem'\n",
    "            }),\n",
    "            html.P(\"Avg Completion (months)\", style={\n",
    "                'color': COLORS['text'], 'margin': '5px 0 15px 0', 'fontSize': '0.9rem',\n",
    "                'fontFamily': 'Rajdhani, monospace'\n",
    "            })\n",
    "        ]),\n",
    "        html.Div([\n",
    "            html.H3(f\"{pass_rate:.1f}%\" if pass_rate > 0 else \"N/A\", style={\n",
    "                'color': COLORS['neon_purple'], 'fontWeight': '900', 'margin': '0',\n",
    "                'fontFamily': 'Orbitron, monospace', 'fontSize': '2rem'\n",
    "            }),\n",
    "            html.P(\"Pass Rate\", style={\n",
    "                'color': COLORS['text'], 'margin': '5px 0 15px 0', 'fontSize': '0.9rem',\n",
    "                'fontFamily': 'Rajdhani, monospace'\n",
    "            })\n",
    "        ])\n",
    "    ])\n",
    "    \n",
    "    # Create student data table - show first 10 by default, filter by search if provided\n",
    "    if search_value:\n",
    "        # Apply search filter only for display\n",
    "        search_filtered = df[df['STUDENT ID'].astype(str).str.contains(str(search_value), na=False, case=False)]\n",
    "        display_students = search_filtered.head(10)  # Show top 10 matches\n",
    "    else:\n",
    "        # Show first 10 students by default\n",
    "        display_students = df.head(10)\n",
    "    \n",
    "    student_cards = []\n",
    "    for _, row in display_students.iterrows():\n",
    "        # Build card with available columns\n",
    "        card_content = [\n",
    "            html.P(f\"ID: {row['STUDENT ID']}\", style={\n",
    "                'color': COLORS['neon_blue'], 'fontWeight': 'bold', 'margin': '5px 0',\n",
    "                'fontFamily': 'Orbitron, monospace'\n",
    "            })\n",
    "        ]\n",
    "        \n",
    "        # Add available information\n",
    "        if 'GENDER' in row and pd.notna(row['GENDER']):\n",
    "            card_content.append(html.P(f\"Gender: {row['GENDER']}\", style={\n",
    "                'color': COLORS['text'], 'margin': '3px 0', 'fontSize': '0.9rem',\n",
    "                'fontFamily': 'Rajdhani, monospace'\n",
    "            }))\n",
    "        \n",
    "        if 'CITIZENSHIP' in row and pd.notna(row['CITIZENSHIP']):\n",
    "            card_content.append(html.P(f\"Citizenship: {row['CITIZENSHIP']}\", style={\n",
    "                'color': COLORS['text'], 'margin': '3px 0', 'fontSize': '0.9rem',\n",
    "                'fontFamily': 'Rajdhani, monospace'\n",
    "            }))\n",
    "        \n",
    "        if 'CUMULATIVE_GPA' in row and pd.notna(row['CUMULATIVE_GPA']):\n",
    "            card_content.append(html.P(f\"GPA: {row['CUMULATIVE_GPA']:.2f}\", style={\n",
    "                'color': COLORS['neon_green'], 'fontWeight': 'bold', 'margin': '3px 0',\n",
    "                'fontFamily': 'Rajdhani, monospace'\n",
    "            }))\n",
    "        \n",
    "        if 'COURSE FUNDING' in row and pd.notna(row['COURSE FUNDING']):\n",
    "            card_content.append(html.P(f\"Funding: {row['COURSE FUNDING']}\", style={\n",
    "                'color': COLORS['text'], 'margin': '3px 0', 'fontSize': '0.9rem',\n",
    "                'fontFamily': 'Rajdhani, monospace'\n",
    "            }))\n",
    "        \n",
    "        if 'PERFORMANCE_TIER' in row and pd.notna(row['PERFORMANCE_TIER']):\n",
    "            card_content.append(html.P(f\"Performance: {row['PERFORMANCE_TIER']}\", style={\n",
    "                'color': COLORS['accent'], 'fontWeight': 'bold', 'margin': '3px 0',\n",
    "                'fontFamily': 'Rajdhani, monospace'\n",
    "            }))\n",
    "        \n",
    "        # Add separator\n",
    "        card_content.append(html.Hr(style={'borderColor': COLORS['text_dim'], 'margin': '10px 0'}))\n",
    "        \n",
    "        card = html.Div(card_content, style={\n",
    "            'padding': '10px', 'margin': '5px 0',\n",
    "            'border': f'1px solid {COLORS[\"text_dim\"]}40',\n",
    "            'borderRadius': '10px',\n",
    "            'backgroundColor': f'{COLORS[\"card_bg\"]}60'\n",
    "        })\n",
    "        student_cards.append(card)\n",
    "    \n",
    "    student_table = html.Div(student_cards)\n",
    "    \n",
    "    # Return data for charts (date-filtered only, no search filter)\n",
    "    return student_table, kpi_display, chart_filtered_df.to_dict('records')\n",
    "\n",
    "# Chart callbacks to display your existing figures with dynamic data AND preserve your interactive filters\n",
    "@app.callback(Output('chart-1', 'figure'), Input('filtered-data', 'data'))\n",
    "def update_chart_1(filtered_data):\n",
    "    if not filtered_data:\n",
    "        return fig1  # Return original with all your filters intact\n",
    "    \n",
    "    # Convert filtered data back to DataFrame\n",
    "    filtered_df = pd.DataFrame(filtered_data)\n",
    "    \n",
    "    if len(filtered_df) == 0:\n",
    "        # Create EMPTY chart with \"No Data\" message\n",
    "        fig_empty = px.treemap(\n",
    "            pd.DataFrame({'x': ['No Data Found'], 'y': [1]}),\n",
    "            path=['x'],\n",
    "            values='y',\n",
    "            title='<b>🚫 No Students Found in Selected Date Range</b><br><sub>Adjust your date filters or click \"All Time\" to see all data</sub>'\n",
    "        )\n",
    "        fig_empty.update_layout(\n",
    "            font=dict(family='Orbitron, monospace', size=12, color=COLORS['light']),\n",
    "            title_font_size=18,\n",
    "            title_x=0.5,\n",
    "            title_font_color=COLORS['danger'],\n",
    "            paper_bgcolor=COLORS['dark_bg'],\n",
    "            height=700,\n",
    "            margin=dict(t=150, l=20, r=20, b=20)\n",
    "        )\n",
    "        fig_empty.update_traces(\n",
    "            textfont_color=COLORS['danger'],\n",
    "            marker_colorscale=[[0, COLORS['danger']], [1, COLORS['danger']]]\n",
    "        )\n",
    "        return fig_empty\n",
    "    \n",
    "    # Regenerate treemap with filtered data but KEEP the original structure\n",
    "    treemap_data = filtered_df.groupby(['CITIZENSHIP', 'GENDER', 'COURSE FUNDING']).size().reset_index(name='COUNT')\n",
    "    treemap_data['PERCENTAGE'] = (treemap_data['COUNT'] / len(filtered_df) * 100).round(1)\n",
    "    \n",
    "    fig_updated = px.treemap(\n",
    "        treemap_data,\n",
    "        path=['CITIZENSHIP', 'GENDER', 'COURSE FUNDING'],\n",
    "        values='COUNT',\n",
    "        title=f'<b>🌍 Student Population Breakdown ({len(filtered_df)} students)</b><br><sub>Distribution by Citizenship, Gender, and Funding Type • Click to drill down</sub>',\n",
    "        color='COUNT',\n",
    "        color_continuous_scale='Viridis',\n",
    "        hover_data={'PERCENTAGE': ':.1f%'}\n",
    "    )\n",
    "    \n",
    "    fig_updated.update_layout(\n",
    "        font=dict(family='Orbitron, monospace', size=12, color=COLORS['light']),\n",
    "        title_font_size=18,\n",
    "        title_x=0.5,\n",
    "        title_font_color=COLORS['light'],\n",
    "        paper_bgcolor=COLORS['dark_bg'],\n",
    "        height=700,\n",
    "        margin=dict(t=150, l=20, r=20, b=20)\n",
    "    )\n",
    "    \n",
    "    fig_updated.update_traces(\n",
    "        textinfo='label+value+percent parent',\n",
    "        textfont_size=11,\n",
    "        textfont_color=COLORS['light'],\n",
    "        hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{customdata[0]:.1f}%<extra></extra>'\n",
    "    )\n",
    "    \n",
    "    return fig_updated\n",
    "\n",
    "@app.callback(Output('chart-2', 'figure'), Input('filtered-data', 'data'))\n",
    "def update_chart_2(filtered_data):\n",
    "    if not filtered_data:\n",
    "        return fig2  # Return original with ALL your interactive features\n",
    "    \n",
    "    # Convert filtered data back to DataFrame\n",
    "    filtered_df = pd.DataFrame(filtered_data)\n",
    "    \n",
    "    if len(filtered_df) == 0:\n",
    "        # Create EMPTY scatter plot with \"No Data\" message\n",
    "        fig_empty = go.Figure()\n",
    "        fig_empty.add_trace(go.Scatter(\n",
    "            x=[0], y=[2.5], mode='text',\n",
    "            text=['No Data Found<br>Adjust date filters or click \"All Time\"'],\n",
    "            textfont=dict(size=20, color=COLORS['danger'], family='Orbitron, monospace'),\n",
    "            showlegend=False\n",
    "        ))\n",
    "        fig_empty.update_layout(\n",
    "            title=dict(\n",
    "                text='<b>🚫 No Students Found in Selected Date Range</b><br><sub>GPA vs Completion Time Analysis - No data to display</sub>',\n",
    "                font=dict(size=20, family='Orbitron, monospace', color=COLORS['danger']),\n",
    "                x=0.5, y=0.95\n",
    "            ),\n",
    "            xaxis=dict(\n",
    "                title=dict(text='Completion Time (Months)', font=dict(size=14, family='Orbitron, monospace', color=COLORS['neon_blue'])),\n",
    "                tickfont=dict(size=12, family='Orbitron, monospace', color=COLORS['text']),\n",
    "                gridcolor='rgba(200,200,200,0.2)', gridwidth=1, range=[0, 10]\n",
    "            ),\n",
    "            yaxis=dict(\n",
    "                title=dict(text='Cumulative GPA', font=dict(size=14, family='Orbitron, monospace', color=COLORS['neon_purple'])),\n",
    "                tickfont=dict(size=12, family='Orbitron, monospace', color=COLORS['text']),\n",
    "                gridcolor='rgba(200,200,200,0.2)', gridwidth=1, range=[1.0, 4.0]\n",
    "            ),\n",
    "            font=dict(family='Orbitron, monospace', size=12, color=COLORS['light']),\n",
    "            paper_bgcolor=COLORS['dark_bg'], plot_bgcolor='rgba(0,0,0,0)',\n",
    "            height=700, margin=dict(t=150, l=80, r=120, b=80), showlegend=False\n",
    "        )\n",
    "        return fig_empty\n",
    "    \n",
    "    # Recreate your FULL interactive scatter plot with ALL original features\n",
    "    scatter_data = filtered_df.dropna(subset=['CUMULATIVE_GPA', 'COMPLETION_MONTHS'])\n",
    "    \n",
    "    if len(scatter_data) == 0:\n",
    "        return fig2\n",
    "    \n",
    "    # Fix None values in SUCCESS_SCORE and RISK_SCORE\n",
    "    scatter_data = scatter_data.copy()\n",
    "    if 'SUCCESS_SCORE' not in scatter_data.columns or scatter_data['SUCCESS_SCORE'].isna().all():\n",
    "        # Create success score if missing or all None\n",
    "        scatter_data['SUCCESS_SCORE'] = (scatter_data['CUMULATIVE_GPA'] / 4.0 * 50) + \\\n",
    "                                       ((scatter_data['COMPLETION_MONTHS'].max() - scatter_data['COMPLETION_MONTHS']) / \n",
    "                                        scatter_data['COMPLETION_MONTHS'].max() * 50)\n",
    "    else:\n",
    "        # Fill None values with calculated score\n",
    "        mask = scatter_data['SUCCESS_SCORE'].isna()\n",
    "        scatter_data.loc[mask, 'SUCCESS_SCORE'] = (scatter_data.loc[mask, 'CUMULATIVE_GPA'] / 4.0 * 50) + \\\n",
    "                                                 ((scatter_data['COMPLETION_MONTHS'].max() - scatter_data.loc[mask, 'COMPLETION_MONTHS']) / \n",
    "                                                  scatter_data['COMPLETION_MONTHS'].max() * 50)\n",
    "    \n",
    "    if 'RISK_SCORE' not in scatter_data.columns or scatter_data['RISK_SCORE'].isna().all():\n",
    "        scatter_data['RISK_SCORE'] = 1 - (scatter_data['SUCCESS_SCORE'] / 100)\n",
    "    else:\n",
    "        # Fill None values\n",
    "        mask = scatter_data['RISK_SCORE'].isna()\n",
    "        scatter_data.loc[mask, 'RISK_SCORE'] = 1 - (scatter_data.loc[mask, 'SUCCESS_SCORE'] / 100)\n",
    "        \n",
    "    if 'RISK_CATEGORY' not in scatter_data.columns:\n",
    "        scatter_data['RISK_CATEGORY'] = pd.cut(scatter_data['RISK_SCORE'], \n",
    "                                             bins=[0, 0.3, 0.7, 1.0], \n",
    "                                             labels=['Low Risk', 'Medium Risk', 'High Risk'])\n",
    "    \n",
    "    fig_updated = go.Figure()\n",
    "    \n",
    "    # Recreate ALL your original traces with citizenship filtering\n",
    "    citizenship_types = scatter_data['CITIZENSHIP'].unique()\n",
    "    for i, citizenship in enumerate(citizenship_types):\n",
    "        citizenship_subset = scatter_data[scatter_data['CITIZENSHIP'] == citizenship]\n",
    "        \n",
    "        # Regular traces\n",
    "        fig_updated.add_trace(go.Scatter(\n",
    "            x=citizenship_subset['COMPLETION_MONTHS'],\n",
    "            y=citizenship_subset['CUMULATIVE_GPA'],\n",
    "            mode='markers',\n",
    "            marker=dict(\n",
    "                size=12 + (citizenship_subset['RISK_SCORE'] * 4),\n",
    "                color=citizenship_subset['SUCCESS_SCORE'],  # Now guaranteed to be numeric\n",
    "                colorscale='Viridis',\n",
    "                showscale=True if i == 0 else False,\n",
    "                colorbar=dict(\n",
    "                    title=\"Success<br>Score<br>(0-100)\",\n",
    "                    titlefont=dict(size=12, family='Arial Black'),\n",
    "                    tickfont=dict(size=10),\n",
    "                    len=0.8\n",
    "                ) if i == 0 else None,\n",
    "                line=dict(width=2, color='white'),\n",
    "                opacity=0.8,\n",
    "                symbol='circle'\n",
    "            ),\n",
    "            text=[f\"Student ID: {row['STUDENT ID']}<br>\" +\n",
    "                  f\"GPA: {row['CUMULATIVE_GPA']:.2f}<br>\" +\n",
    "                  f\"Completion: {row['COMPLETION_MONTHS']:.1f} months<br>\" +\n",
    "                  f\"Success Score: {row['SUCCESS_SCORE']:.1f}<br>\" +\n",
    "                  f\"Risk Category: {row['RISK_CATEGORY']}<br>\" +\n",
    "                  f\"Citizenship: {row['CITIZENSHIP']}<br>\" +\n",
    "                  f\"Gender: {row['GENDER']}<br>\" +\n",
    "                  f\"Funding: {row['COURSE FUNDING']}\"\n",
    "                  for _, row in citizenship_subset.iterrows()],\n",
    "            hovertemplate='%{text}<extra></extra>',\n",
    "            name=f'{citizenship} ({len(citizenship_subset)} students)',\n",
    "            visible=True\n",
    "        ))\n",
    "    \n",
    "    # Add HIGH ACHIEVERS traces (preserving your logic)\n",
    "    for i, citizenship in enumerate(citizenship_types):\n",
    "        high_achievers = scatter_data[(scatter_data['CITIZENSHIP'] == citizenship) & \n",
    "                                     (scatter_data['CUMULATIVE_GPA'] > 3.5) &\n",
    "                                     (scatter_data['COMPLETION_MONTHS'] < 5)]\n",
    "        \n",
    "        fig_updated.add_trace(go.Scatter(\n",
    "            x=high_achievers['COMPLETION_MONTHS'],\n",
    "            y=high_achievers['CUMULATIVE_GPA'],\n",
    "            mode='markers',\n",
    "            marker=dict(\n",
    "                size=12 + (high_achievers['RISK_SCORE'] * 4) if 'RISK_SCORE' in high_achievers.columns else 12,\n",
    "                color=high_achievers['SUCCESS_SCORE'] if 'SUCCESS_SCORE' in high_achievers.columns else citizenship_colors[i % len(citizenship_colors)],\n",
    "                colorscale='Viridis',\n",
    "                showscale=False,\n",
    "                line=dict(width=2, color='white'),\n",
    "                opacity=0.8,\n",
    "                symbol='circle'\n",
    "            ),\n",
    "            text=[f\"Student ID: {row['STUDENT ID']}<br>\" +\n",
    "                  f\"GPA: {row['CUMULATIVE_GPA']:.2f} ⭐⭐<br>\" +\n",
    "                  f\"Completion: {row['COMPLETION_MONTHS']:.1f} months 🚀<br>\" +\n",
    "                  f\"Success Score: {row.get('SUCCESS_SCORE', 'N/A')}<br>\" +\n",
    "                  f\"Risk Category: {row.get('RISK_CATEGORY', 'N/A')}<br>\" +\n",
    "                  f\"Citizenship: {row['CITIZENSHIP']}<br>\" +\n",
    "                  f\"Gender: {row['GENDER']}<br>\" +\n",
    "                  f\"Funding: {row['COURSE FUNDING']}\"\n",
    "                  for _, row in high_achievers.iterrows()],\n",
    "            hovertemplate='%{text}<extra></extra>',\n",
    "            name=f'{citizenship} High Achievers ({len(high_achievers)} students)',\n",
    "            visible=False\n",
    "        ))\n",
    "    \n",
    "    # Add UNDERPERFORMERS traces (preserving your logic)\n",
    "    for i, citizenship in enumerate(citizenship_types):\n",
    "        underperformers = scatter_data[(scatter_data['CITIZENSHIP'] == citizenship) & \n",
    "                                      (scatter_data['CUMULATIVE_GPA'] < 2.5)]\n",
    "        \n",
    "        fig_updated.add_trace(go.Scatter(\n",
    "            x=underperformers['COMPLETION_MONTHS'],\n",
    "            y=underperformers['CUMULATIVE_GPA'],\n",
    "            mode='markers',\n",
    "            marker=dict(\n",
    "                size=12 + (underperformers['RISK_SCORE'] * 4) if 'RISK_SCORE' in underperformers.columns else 12,\n",
    "                color=underperformers['SUCCESS_SCORE'] if 'SUCCESS_SCORE' in underperformers.columns else citizenship_colors[i % len(citizenship_colors)],\n",
    "                colorscale='Viridis',\n",
    "                showscale=False,\n",
    "                line=dict(width=2, color='white'),\n",
    "                opacity=0.8,\n",
    "                symbol='circle'\n",
    "            ),\n",
    "            text=[f\"Student ID: {row['STUDENT ID']}<br>\" +\n",
    "                  f\"GPA: {row['CUMULATIVE_GPA']:.2f} 🚨<br>\" +\n",
    "                  f\"Completion: {row['COMPLETION_MONTHS']:.1f} months<br>\" +\n",
    "                  f\"Success Score: {row.get('SUCCESS_SCORE', 'N/A')}<br>\" +\n",
    "                  f\"Risk Category: {row.get('RISK_CATEGORY', 'N/A')}<br>\" +\n",
    "                  f\"Citizenship: {row['CITIZENSHIP']}<br>\" +\n",
    "                  f\"Gender: {row['GENDER']}<br>\" +\n",
    "                  f\"Funding: {row['COURSE FUNDING']}\"\n",
    "                  for _, row in underperformers.iterrows()],\n",
    "            hovertemplate='%{text}<extra></extra>',\n",
    "            name=f'{citizenship} Underperformers ({len(underperformers)} students)',\n",
    "            visible=False\n",
    "        ))\n",
    "    \n",
    "    # Recreate ALL your dropdown buttons (preserving your original logic)\n",
    "    num_citizenship = len(citizenship_types)\n",
    "    dropdown_buttons = [\n",
    "        # Show all citizenship types (regular view)\n",
    "        dict(label='🌍 All Citizenship Types', \n",
    "             method='update', \n",
    "             args=[{'visible': [True] * num_citizenship + [False] * (num_citizenship * 2)}]),\n",
    "    ]\n",
    "    \n",
    "    # Add individual citizenship options (regular view)\n",
    "    for i, citizenship in enumerate(citizenship_types):\n",
    "        visibility = [False] * (num_citizenship * 3)\n",
    "        visibility[i] = True\n",
    "        dropdown_buttons.append(\n",
    "            dict(label=f'🎯 {citizenship} Only',\n",
    "                 method='update',\n",
    "                 args=[{'visible': visibility}])\n",
    "        )\n",
    "    \n",
    "    # Add high achievers view\n",
    "    high_achiever_visibility = [False] * num_citizenship + [True] * num_citizenship + [False] * num_citizenship\n",
    "    dropdown_buttons.append(\n",
    "        dict(label='⭐ High Achievers (GPA > 3.5 & < 5 months)', \n",
    "             method='update', \n",
    "             args=[{'visible': high_achiever_visibility}])\n",
    "    )\n",
    "    \n",
    "    # Add underperformers view\n",
    "    underperformer_visibility = [False] * (num_citizenship * 2) + [True] * num_citizenship\n",
    "    dropdown_buttons.append(\n",
    "        dict(label='🚨 Underperformers (GPA < 2.5)', \n",
    "             method='update', \n",
    "             args=[{'visible': underperformer_visibility}])\n",
    "    )\n",
    "    \n",
    "    fig_updated.update_layout(\n",
    "        title=dict(\n",
    "            text=f'<b>🎯 Interactive GPA vs Completion Time Analysis ({len(filtered_df)} students)</b><br>' +\n",
    "                 '<sub>Success score by color • Risk level by marker size • Use filters to explore different groups</sub>',\n",
    "            font=dict(size=20, family='Orbitron, monospace', color=COLORS['light']),\n",
    "            x=0.5,\n",
    "            y=0.95\n",
    "        ),\n",
    "        xaxis=dict(\n",
    "            title=dict(text='Completion Time (Months)', font=dict(size=14, family='Orbitron, monospace', color=COLORS['neon_blue'])),\n",
    "            tickfont=dict(size=12, family='Orbitron, monospace', color=COLORS['text']),\n",
    "            gridcolor='rgba(200,200,200,0.2)',\n",
    "            gridwidth=1,\n",
    "            range=[0, max(scatter_data['COMPLETION_MONTHS']) + 5] if len(scatter_data) > 0 else [0, 10]\n",
    "        ),\n",
    "        yaxis=dict(\n",
    "            title=dict(text='Cumulative GPA', font=dict(size=14, family='Orbitron, monospace', color=COLORS['neon_purple'])),\n",
    "            tickfont=dict(size=12, family='Orbitron, monospace', color=COLORS['text']),\n",
    "            gridcolor='rgba(200,200,200,0.2)',\n",
    "            gridwidth=1,\n",
    "            range=[1.0, 4.0]\n",
    "        ),\n",
    "        font=dict(family='Orbitron, monospace', size=12, color=COLORS['light']),\n",
    "        paper_bgcolor=COLORS['dark_bg'],\n",
    "        plot_bgcolor='rgba(0,0,0,0)',\n",
    "        height=700,\n",
    "        margin=dict(t=150, l=80, r=120, b=80),\n",
    "        showlegend=True,\n",
    "        legend=dict(\n",
    "            orientation='v',\n",
    "            yanchor='top',\n",
    "            y=0.98,\n",
    "            xanchor='left',\n",
    "            x=1.02,\n",
    "            bgcolor=COLORS['card_bg'],\n",
    "            bordercolor=COLORS['neon_blue'],\n",
    "            borderwidth=1,\n",
    "            font=dict(color=COLORS['light'])\n",
    "        ),\n",
    "        \n",
    "        # PRESERVE your interactive dropdown menu\n",
    "        updatemenus=[\n",
    "            dict(\n",
    "                buttons=dropdown_buttons,\n",
    "                direction=\"down\",\n",
    "                showactive=True,\n",
    "                x=0.02,\n",
    "                xanchor=\"left\",\n",
    "                y=1.12,\n",
    "                yanchor=\"top\",\n",
    "                bgcolor=COLORS['card_bg'],\n",
    "                bordercolor=COLORS['neon_green'],\n",
    "                borderwidth=2,\n",
    "                font=dict(color=COLORS['light'])\n",
    "            )\n",
    "        ],\n",
    "        \n",
    "        # PRESERVE your filter label\n",
    "        annotations=[\n",
    "            dict(\n",
    "                text=\"🔍 Filter by Group:\",\n",
    "                x=0.02, y=1.18,\n",
    "                xref=\"paper\", yref=\"paper\",\n",
    "                showarrow=False,\n",
    "                font=dict(size=12, family='Orbitron, monospace', color=COLORS['neon_green'])\n",
    "            )\n",
    "        ]\n",
    "    )\n",
    "    \n",
    "    # Add reference lines (preserving your original styling)\n",
    "    fig_updated.add_hline(y=2.0, line_dash=\"dot\", line_color=COLORS['danger'], line_width=2, opacity=0.8, \n",
    "                          annotation_text=\"Pass Threshold (2.0)\")\n",
    "    fig_updated.add_hline(y=3.5, line_dash=\"dot\", line_color=COLORS['success'], line_width=2, opacity=0.8, \n",
    "                          annotation_text=\"Excellence Threshold (3.5)\")\n",
    "    \n",
    "    return fig_updated\n",
    "\n",
    "@app.callback(Output('chart-3', 'figure'), Input('filtered-data', 'data'))\n",
    "def update_chart_3(filtered_data):\n",
    "    if not filtered_data:\n",
    "        return fig3  # Return original with ALL your dropdowns\n",
    "    \n",
    "    # Convert filtered data back to DataFrame\n",
    "    filtered_df = pd.DataFrame(filtered_data)\n",
    "    \n",
    "    if len(filtered_df) == 0:\n",
    "        # Create EMPTY box plot with \"No Data\" message\n",
    "        fig_empty = go.Figure()\n",
    "        fig_empty.add_trace(go.Scatter(\n",
    "            x=[0], y=[15], mode='text',\n",
    "            text=['No Data Found<br>Adjust date filters or click \"All Time\"'],\n",
    "            textfont=dict(size=20, color=COLORS['danger'], family='Orbitron, monospace'),\n",
    "            showlegend=False\n",
    "        ))\n",
    "        fig_empty.update_layout(\n",
    "            title='<b>🚫 No Students Found in Selected Date Range</b><br><sub>Completion Time Distribution - No data to display</sub>',\n",
    "            title_font_size=18, title_x=0.5, title_font_color=COLORS['danger'],\n",
    "            yaxis_title='Completion Time (Months)', xaxis_title='Citizenship Status',\n",
    "            font=dict(family='Orbitron, monospace', size=12, color=COLORS['light']),\n",
    "            paper_bgcolor=COLORS['dark_bg'], plot_bgcolor='rgba(0,0,0,0)',\n",
    "            height=700, margin=dict(t=150, l=80, r=80, b=80), showlegend=False,\n",
    "            yaxis=dict(gridcolor='rgba(200,200,200,0.2)', gridwidth=1, range=[0, 30],\n",
    "                      title_font_color=COLORS['neon_green'], tickfont=dict(color=COLORS['text'])),\n",
    "            xaxis=dict(gridcolor='rgba(200,200,200,0.2)', gridwidth=1,\n",
    "                      title_font_color=COLORS['neon_blue'], tickfont=dict(color=COLORS['text']))\n",
    "        )\n",
    "        return fig_empty\n",
    "    \n",
    "    # Regenerate box plot with filtered data but PRESERVE all your dropdown functionality\n",
    "    completion_data = filtered_df.dropna(subset=['COMPLETION_MONTHS'])\n",
    "    completion_data = completion_data[completion_data['COMPLETION_MONTHS'] > 0]\n",
    "    completion_data = completion_data[completion_data['COMPLETION_MONTHS'] <= 60]\n",
    "    \n",
    "    if len(completion_data) == 0:\n",
    "        return fig3\n",
    "    \n",
    "    fig_updated = go.Figure()\n",
    "    \n",
    "    # Add box plot for each citizenship type in filtered data (preserving your structure)\n",
    "    for i, citizenship in enumerate(completion_data['CITIZENSHIP'].unique()):\n",
    "        citizenship_data = completion_data[completion_data['CITIZENSHIP'] == citizenship]\n",
    "        \n",
    "        fig_updated.add_trace(\n",
    "            go.Box(\n",
    "                y=citizenship_data['COMPLETION_MONTHS'],\n",
    "                name=citizenship,\n",
    "                marker_color=citizenship_colors[i % len(citizenship_colors)],\n",
    "                boxpoints='outliers',\n",
    "                jitter=0.3,\n",
    "                pointpos=-1.8,\n",
    "                marker=dict(\n",
    "                    size=4,\n",
    "                    opacity=0.6,\n",
    "                    line=dict(width=1, color='white')\n",
    "                ),\n",
    "                hovertemplate='<b>%{fullData.name}</b><br>' +\n",
    "                             'Completion Time: %{y:.1f} months<br>' +\n",
    "                             'Student Count: ' + str(len(citizenship_data)) + '<br>' +\n",
    "                             '<extra></extra>',\n",
    "                visible=True\n",
    "            )\n",
    "        )\n",
    "    \n",
    "    # Recreate YOUR dropdown buttons (preserving original logic)\n",
    "    all_visible = [True] * len(completion_data['CITIZENSHIP'].unique())\n",
    "    dropdown_buttons = [\n",
    "        dict(label='All Citizenship Types',\n",
    "             method='update',\n",
    "             args=[{'visible': all_visible}])\n",
    "    ]\n",
    "    \n",
    "    # Add individual citizenship type options (preserving your logic)\n",
    "    for i, citizenship in enumerate(completion_data['CITIZENSHIP'].unique()):\n",
    "        visibility = [False] * len(completion_data['CITIZENSHIP'].unique())\n",
    "        visibility[i] = True\n",
    "        dropdown_buttons.append(\n",
    "            dict(label=f'{citizenship} Only',\n",
    "                 method='update',\n",
    "                 args=[{'visible': visibility}])\n",
    "        )\n",
    "    \n",
    "    fig_updated.update_layout(\n",
    "        title=f'<b>🔍 Course Completion Time Distribution ({len(filtered_df)} students)</b><br><sub>Interactive box plot analysis of completion duration by citizenship status</sub>',\n",
    "        title_font_size=18,\n",
    "        title_x=0.5,\n",
    "        title_font_color=COLORS['light'],\n",
    "        yaxis_title='Completion Time (Months)',\n",
    "        xaxis_title='Citizenship Status',\n",
    "        font=dict(family='Orbitron, monospace', size=12, color=COLORS['light']),\n",
    "        paper_bgcolor=COLORS['dark_bg'],\n",
    "        plot_bgcolor='rgba(0,0,0,0)',\n",
    "        height=700,\n",
    "        margin=dict(t=150, l=80, r=80, b=80),\n",
    "        showlegend=False,\n",
    "        \n",
    "        # PRESERVE your dropdown functionality\n",
    "        updatemenus=[\n",
    "            dict(\n",
    "                buttons=dropdown_buttons,\n",
    "                direction='down',\n",
    "                showactive=True,\n",
    "                x=0.02,\n",
    "                xanchor='left',\n",
    "                y=1.12,\n",
    "                yanchor='top',\n",
    "                bgcolor=COLORS['card_bg'],\n",
    "                bordercolor=COLORS['neon_purple'],\n",
    "                borderwidth=2,\n",
    "                font=dict(color=COLORS['light'])\n",
    "            )\n",
    "        ],\n",
    "        annotations=[\n",
    "            dict(\n",
    "                text=\"🔍 Filter Options:\",\n",
    "                x=0.02, y=1.18,\n",
    "                xref=\"paper\", yref=\"paper\",\n",
    "                showarrow=False,\n",
    "                font=dict(size=12, family='Orbitron, monospace', color=COLORS['neon_purple'])\n",
    "            )\n",
    "        ],\n",
    "        yaxis=dict(\n",
    "            gridcolor='rgba(200,200,200,0.2)',\n",
    "            gridwidth=1,\n",
    "            range=[0, 60],\n",
    "            title_font_color=COLORS['neon_green'],\n",
    "            tickfont=dict(color=COLORS['text'])\n",
    "        ),\n",
    "        xaxis=dict(\n",
    "            gridcolor='rgba(200,200,200,0.2)',\n",
    "            gridwidth=1,\n",
    "            title_font_color=COLORS['neon_blue'],\n",
    "            tickfont=dict(color=COLORS['text'])\n",
    "        )\n",
    "    )\n",
    "    \n",
    "    return fig_updated\n",
    "\n",
    "@app.callback(Output('chart-4', 'figure'), Input('filtered-data', 'data'))\n",
    "def update_chart_4(filtered_data):\n",
    "    # For the animated chart, preserve it exactly as you made it\n",
    "    if not filtered_data:\n",
    "        return fig4\n",
    "    \n",
    "    filtered_df = pd.DataFrame(filtered_data)\n",
    "    total_filtered = len(filtered_df)\n",
    "    total_original = len(df)\n",
    "    \n",
    "    # Clone the original figure and update title to show filter status\n",
    "    fig_updated = go.Figure(fig4)\n",
    "    fig_updated.update_layout(\n",
    "        title=f'<b>📈 Temporal Trends ({total_filtered}/{total_original} students)</b><br><sub>Animated progression over academic periods</sub>'\n",
    "    )\n",
    "    \n",
    "    return fig_updated\n",
    "\n",
    "# Live time update callback\n",
    "@app.callback(\n",
    "    Output('live-time', 'children'),\n",
    "    Input('interval-update', 'n_intervals')\n",
    ")\n",
    "def update_time(n):\n",
    "    from datetime import datetime\n",
    "    return datetime.now().strftime('%H:%M:%S')\n",
    "\n",
    "# \"All Time\" button callback to reset date pickers to original data range\n",
    "@app.callback(\n",
    "    [Output('start-date-picker', 'date'),\n",
    "     Output('end-date-picker', 'date')],\n",
    "    Input('btn-all-years', 'n_clicks'),\n",
    "    prevent_initial_call=True\n",
    ")\n",
    "def reset_date_filters(n_clicks):\n",
    "    if n_clicks:\n",
    "        # Reset to the actual data range in your dataset\n",
    "        return datetime(2022, 4, 18), datetime(2025, 4, 24)\n",
    "    return datetime(2022, 4, 1), datetime(2025, 4, 24)\n",
    "\n",
    "print(\"✅ All callbacks configured with your actual data structure!\")\n",
    "print(f\"📊 Dashboard ready for {len(df)} students with real metrics!\")\n",
    "print(\"🔄 Charts will now show EMPTY when no data matches filters!\")\n",
    "print(\"⏰ 'All Time' button will reset date range automatically!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "b8281a50",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "🌟 Dashboard will be available at: http://127.0.0.1:8052/\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"100%\"\n",
       "            height=\"650\"\n",
       "            src=\"http://127.0.0.1:8052/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x24a3afd1d90>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# === LAUNCH DASHBOARD ===\n",
    "if __name__ == '__main__':\n",
    "    \n",
    "    print(\"🌟 Dashboard will be available at: http://127.0.0.1:8052/\")\n",
    "   \n",
    "    \n",
    "    app.run(debug=True, port=8052)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
