---
title: "CSCI 117 Intro Survey"
published: true
morea_id: grade1
morea_type: assessment
morea_outcomes_assessed:
  - outcome1
morea_sort_order: 0
---

<link rel="stylesheet" href="http://cdn.oesmith.co.uk/morris-0.4.3.min.css">
<script src="//cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.js"></script>
<script src="http://cdn.oesmith.co.uk/morris-0.4.3.min.js"></script>

<div class="well" style="width: 450px">
  <div id="assessment" style="width: 400px; height: 250px"></div>
  Assess course motivation, understanding of course structure, and what is computer science.
</div>

<script>
Morris.Bar({
  element: 'assessment',
  hideHover: false,
  data: [
        { y: 'Satisfactory (%)', num: 27 },
        { y: 'Unsatisfactory (%)', num: 3 },
        ],
  xkey: 'y',
  ykeys: ['num'],
  resize: true,
  labels: ['Students']
});
</script>
