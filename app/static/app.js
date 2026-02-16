const kpis = [
  { label: 'Total Calls (Today)', value: '1,284', trend: '+11.8% vs yesterday', trendClass: 'up' },
  { label: 'Connected Calls', value: '736', trend: '57.3% connect rate', trendClass: 'up' },
  { label: 'Converted Leads', value: '182', trend: '24.7% from connected', trendClass: 'up' },
  { label: 'Average Handle Time', value: '03:46', trend: '-4.2% improved', trendClass: 'up' },
  { label: 'AI→Human Transfers', value: '68', trend: '8 pending acceptance', trendClass: 'warn' },
];

const funnel = [
  { stage: 'Leads Assigned', count: 2450 },
  { stage: 'Calls Attempted', count: 1284 },
  { stage: 'Calls Connected', count: 736 },
  { stage: 'Qualified Leads', count: 274 },
  { stage: 'Converted', count: 182 },
];

const transferPool = [
  { agent: 'Rahul Menon', skill: 'Insurance', status: 'Available (0/2)' },
  { agent: 'Sneha Kapoor', skill: 'Loans', status: 'Available (1/3)' },
  { agent: 'Aman Verma', skill: 'Cards', status: 'Busy (2/2)' },
  { agent: 'Priyanka Das', skill: 'SME Lending', status: 'Available (0/1)' },
];

const leads = [
  {
    name: 'Amit Sharma',
    phone: '+91-98xxxxxx11',
    assignee: 'Human • Rahul',
    status: { label: 'Follow Up', cls: 'followup' },
    priority: 'High',
    updated: 'Requested callback at 5:00 PM'
  },
  {
    name: 'Priya Nair',
    phone: '+91-99xxxxxx21',
    assignee: 'AI Agent • Sales-02',
    status: { label: 'Connected', cls: 'connected' },
    priority: 'Medium',
    updated: 'Needs product brochure on WhatsApp'
  },
  {
    name: 'Karan Gill',
    phone: '+91-97xxxxxx31',
    assignee: 'Human • Sneha',
    status: { label: 'Converted', cls: 'converted' },
    priority: 'High',
    updated: 'Converted to premium annual plan'
  },
];

document.getElementById('kpis').innerHTML = kpis.map((k) => `
  <article class="kpi">
    <div class="label">${k.label}</div>
    <div class="value">${k.value}</div>
    <div class="trend ${k.trendClass}">${k.trend}</div>
  </article>
`).join('');

document.getElementById('funnel').innerHTML = funnel.map((f) => `
  <div class="funnel-item">
    <span>${f.stage}</span>
    <strong>${f.count.toLocaleString('en-IN')}</strong>
  </div>
`).join('');

document.getElementById('transfer-list').innerHTML = transferPool.map((row) => `
  <div class="transfer-item">
    <div>
      <strong>${row.agent}</strong>
      <div>${row.skill}</div>
    </div>
    <strong>${row.status}</strong>
  </div>
`).join('');

document.getElementById('lead-table').innerHTML = leads.map((lead) => `
  <tr>
    <td><strong>${lead.name}</strong></td>
    <td>${lead.phone}</td>
    <td>${lead.assignee}</td>
    <td><span class="status-pill ${lead.status.cls}">${lead.status.label}</span></td>
    <td><span class="priority">${lead.priority}</span></td>
    <td>${lead.updated}</td>
  </tr>
`).join('');
