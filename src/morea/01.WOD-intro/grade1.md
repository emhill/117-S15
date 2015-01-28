---
title: "CSCI 117 Intro Survey"
published: true
morea_id: grade1
morea_type: assessment
morea_outcomes_assessed:
  - outcome1
morea_sort_order: 0
---

Assess course motivation, understanding of course structure, and what is computer science.

<link rel="stylesheet" href="http://cdn.oesmith.co.uk/morris-0.4.3.min.css">
<script src="//cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.js"></script>
<script src="http://cdn.oesmith.co.uk/morris-0.4.3.min.js"></script>

<div class="well">
  <div id="assessment" style="height: 250px;"></div>
</div>

<script>
Morris.Bar({
  element: 'assessment',
  hideHover: false,
  data: [
        { y: 'Satisfactory (%)', num: 18 },
        { y: 'Unsatisfactory (%)', num: 9 },
        ],
  xkey: 'y',
  ykeys: ['num'],
  resize: true,
  labels: ['Students']
});
</script>