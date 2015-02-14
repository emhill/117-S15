---
title: "Code.org Exercises"
published: true
morea_id: grade2
morea_type: assessment
morea_outcomes_assessed:
  - outcome1
morea_sort_order: 0
---

<link rel="stylesheet" href="http://cdn.oesmith.co.uk/morris-0.4.3.min.css">
<script src="//cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.js"></script>
<script src="http://cdn.oesmith.co.uk/morris-0.4.3.min.js"></script>

<div class="well" style="width: 550px">
  <div id="assessment" style="width: 500px; height: 250px"></div>
  Explore the use of the 7 basic programming concepts to draw shapes, dig holes, and help an angry bird get a pig
</div>

<script>
Morris.Bar({
  element: 'assessment',
  hideHover: false,
  data: [
        { y: 'Excellent (%)', num: 11 },
        { y: 'Satisfactory (%)', num: 11 },
        { y: 'Unsatisfactory (%)', num: 6 },
        ],
  xkey: 'y',
  ykeys: ['num'],
  resize: true,
  labels: ['Students']
});
</script>
